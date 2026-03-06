$pdf_mode = 1;
$bibtex_use = 2;
$biber = 'biber %O %B';
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 -file-line-error %O %S';
$out_dir = 'build';
add_cus_dep('bcf', 'bbl', 0, 'run_biber');
sub run_biber {
    return system("biber --output-directory build \"$_[0]\"");
}
