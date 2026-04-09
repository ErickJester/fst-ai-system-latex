"""
Captura todos los estados de los mockups HTML como PNG.
Guarda en figures/mockups/.
Usa click real en los botones demo para respetar event.target.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

BASE = Path(__file__).parent
OUT  = BASE / "figures" / "mockups"
OUT.mkdir(parents=True, exist_ok=True)

VIEWPORT = {"width": 1280, "height": 900}

# (archivo_html, texto_del_botón_o_js, nombre_png, usar_click)
# usar_click=True  → busca botón .demo-btn cuyo onclick contiene el texto y hace click
# usar_click=False → evalúa el JS directamente (para funciones que no usan event)
CAPTURES = [
    # ── Login ──────────────────────────────────────────────────────────
    ("mockup_login.html", "setError(false)", "ui_login_normal",    False),
    ("mockup_login.html", "setError(true)",  "ui_login_error",     False),

    # ── Dashboard investigador ─────────────────────────────────────────
    ("mockup_dashboard_investigador.html", "setState('normal')", "ui_dashboard_normal", True),
    ("mockup_dashboard_investigador.html", "setState('warn')",   "ui_dashboard_alerta", True),
    ("mockup_dashboard_investigador.html", "setState('empty')",  "ui_dashboard_vacio",  True),

    # ── Nuevo experimento ──────────────────────────────────────────────
    ("mockup_nuevo_experimento.html", "setDemo('empty')",      "ui_nuevo_vacio",      True),
    ("mockup_nuevo_experimento.html", "setDemo('filled')",     "ui_nuevo_lleno",      True),
    ("mockup_nuevo_experimento.html", "setDemo('uploading')",  "ui_nuevo_subiendo",   True),
    ("mockup_nuevo_experimento.html", "setDemo('fileerror')",  "ui_nuevo_error",      True),
    ("mockup_nuevo_experimento.html", "setDemo('success')",    "ui_nuevo_exito",      True),
    ("mockup_nuevo_experimento.html", "setDemo('validation')", "ui_nuevo_validacion", True),

    # ── Progreso del análisis ──────────────────────────────────────────
    ("mockup_progreso_analisis.html", "setDemo('proc1')",       "ui_progreso_analizando",    True),
    ("mockup_progreso_analisis.html", "setDemo('done')",        "ui_progreso_completado",    True),
    ("mockup_progreso_analisis.html", "setDemo('err_quality')", "ui_progreso_err_calidad",   True),
    ("mockup_progreso_analisis.html", "setDemo('err_detect')",  "ui_progreso_err_deteccion", True),

    # ── Resultados ─────────────────────────────────────────────────────
    ("mockup_resultados.html", "setDemo('d2only')",    "ui_resultados_dia2",        True),
    ("mockup_resultados.html", "setDemo('both')",      "ui_resultados_comparacion", True),
    ("mockup_resultados.html", "setDemo('minexpand')", "ui_resultados_minutos",     True),

    # ── Panel de administración ────────────────────────────────────────
    ("mockup_admin.html", "setDemo('normal')",     "ui_admin_normal",        True),
    ("mockup_admin.html", "setDemo('diskwarn')",   "ui_admin_disco",         True),
    ("mockup_admin.html", "setDemo('queue')",      "ui_admin_cola",          True),
    ("mockup_admin.html", "setDemo('modal_new')",  "ui_admin_modal_nuevo",   True),
    ("mockup_admin.html", "setDemo('modal_edit')", "ui_admin_modal_editar",  True),
]

async def click_demo_btn(page, js_fragment: str):
    """Hace click en el botón .demo-btn cuyo onclick contiene js_fragment."""
    clicked = await page.evaluate(f"""
        (function() {{
            const btns = document.querySelectorAll('.demo-btn, .db');
            for (const b of btns) {{
                const oc = b.getAttribute('onclick') || '';
                if (oc.includes({repr(js_fragment)})) {{
                    b.click();
                    return true;
                }}
            }}
            return false;
        }})()
    """)
    if not clicked:
        # Fallback: evaluación directa (sin event.target)
        await page.evaluate(js_fragment)

async def capture_all():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        current_file = None
        page = None

        for html_file, js_cmd, name, use_click in CAPTURES:
            # Recargar sólo al cambiar de archivo
            if html_file != current_file:
                if page:
                    await page.close()
                page = await browser.new_page()
                await page.set_viewport_size(VIEWPORT)
                url = (BASE / html_file).as_uri()
                await page.goto(url, wait_until="networkidle")
                current_file = html_file
                print(f"\n  Cargado: {html_file}")

            if use_click:
                await click_demo_btn(page, js_cmd)
            else:
                await page.evaluate(js_cmd)

            await page.wait_for_timeout(400)

            out_path = OUT / f"{name}.png"
            await page.screenshot(path=str(out_path), full_page=True)
            print(f"    OK  {name}.png")

        if page:
            await page.close()
        await browser.close()

asyncio.run(capture_all())
print(f"\nListo. PNGs en: {OUT}")
