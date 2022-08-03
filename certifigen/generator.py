import glob
import os
import shutil
import warnings

import PyPDF2
import typer
from certifigen.config import load_conf


def generate_certificate(
    name: str,
    fout: str,
    path_config: str = "./config.toml",
    path_output: str = "certificates",
    path_tex_template: str = "./main.tex",
):
    """Generates a pdf certificate using as template 'main.tex',
    and replacing any '$TEXT$' it has with `text`.
    Stores the pdf in `folder`, naming it `fout`.

    Parameters
    ----------
    text : str
        Text to include in the pdf
    fout : str
        Name of the output file (without 'pdf' termination)
    path_output : str, optional
        Output folder, by default "certificates"
    path_tex_template : str, optional
        Path to the template tex file, by default "./main.tex"

    Raises
    ------
    ValueError
        Raises error when the certificate has more than one page
    """
    cfg = load_conf(path_config, "certificate")
    cfg.update({"name": name})

    # Read in the base LaTeX file
    with open(path_tex_template, "r") as file:
        filedata = file.read()

    # Replace the text in the certificate
    for key, value in cfg.items():
        filedata = filedata.replace(f"${key.upper()}$", value)

    # Write the file out again
    with open(f"{fout}.tex", "w") as file:
        file.write(filedata)

    # Build LaTeX
    os.system(f"pdflatex {fout}.tex")

    # Move the certificate to the folder
    try:
        shutil.move(f"{fout}.pdf", f"{path_output}/{fout}.pdf")
    except FileNotFoundError as er:
        print(f"[ERROR] File failed: {fout}\nText: {text}\nError: {er}")

    # Remove all other byproducts from LaTeX
    for filename in glob.glob(f"{fout}*"):
        os.remove(filename)

    # Ensure the certificate is only one page long
    file = open(f"{path_output}/{fout}.pdf", "rb")
    readpdf = PyPDF2.PdfFileReader(file)
    if readpdf.numPages > 1:
        warnings.warn(f"[WARNING] Number of pages greater than 1: {fout}")


def main(
    path_config: str = "./config.toml",
    path_output: str = "certificates",
    path_tex_template: str = "./main.tex",
):
    name = "Test Mc. Testing"
    fout = "test"
    if not os.path.exists(path_output):
        os.mkdir(path_output)
    generate_certificate(
        name,
        fout,
        path_config=path_config,
        path_output=path_output,
        path_tex_template=path_tex_template,
    )


if __name__ == "__main__":
    typer.run(main)
