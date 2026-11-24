param([string]$Dir, [int]$Rate = -1)
Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$s.SelectVoice('Microsoft Sabina Desktop')
$s.Rate = $Rate
$s.Volume = 100
$items = Get-Content -Raw -Encoding UTF8 (Join-Path $Dir 'textos.json') | ConvertFrom-Json
$out = Join-Path $Dir 'voz'
New-Item -ItemType Directory -Force $out | Out-Null
foreach ($it in $items) {
    $f = Join-Path $out ($it.id + '.wav')
    $s.SetOutputToWaveFile($f)
    $s.Speak($it.texto)
    $s.SetOutputToNull()
}
$s.Dispose()
Write-Output ('listo: ' + $items.Count)
