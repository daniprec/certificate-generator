import glob
import os
import shutil
import warnings

from typing import Optional
import PyPDF2
import typer
from certifigen.utils.config import load_conf


def generate_certificate(
    name: str,
    fout: Optional[str] = None,
    work: Optional[str] = None,
    is_plenary_speaker: bool = False,
    path_config: str = "./config.toml",
    path_output: str = "certificates",
    path_tex_template: str = "./main.tex",
):
    """Generates a pdf certificate using as template 'main.tex',
    and replacing any '$TEXT$' it has with `text`.
    Stores the pdf in `folder`, naming it `fout`.

    Parameters
    ----------
    name : str
        Name of the participant
    fout : str, optional
        Name of the output file (without 'pdf' termination). By default None
    work : str, optional
        Title of the work presented by the participant, if any. By default None
    is_plenary_speaker : bool, optional
        Whether the participant is a plenary speaker. It must have a work associated.
        By default False
    path_config : str, optional
        Path to the config file, by default "./config.toml"
    path_output : str, optional
        Output folder, by default "certificates"
    path_tex_template : str, optional
        Path to the template tex file, by default "./main.tex"
    """
    fout = name if fout is None else fout
    fout = fout.replace(" ", "_")

    # Load configuration
    cfg = load_conf(path_config, "certificate")
    # Include participant name in the config
    cfg.update({"name": name})

    # Include extra text in the config (work name and plenary speaker)
    if work is None:
        text = "."
    elif is_plenary_speaker:
        text = (
            " as a plenary speaker, and presented the talk entitled"
            "\\begin{center}\\textbf{" + work + "}\\end{center}"
        )
    else:
        text = (
            ", and presented the contribution entitled"
            "\\begin{center}\\textbf{" + work + "}\\end{center}"
        )
    cfg.update({"extra": text})

    # Read in the base LaTeX file
    with open(path_tex_template, "r") as file:
        filedata = file.read()

    # Include logos of organizers
    list_logos = cfg["path_logo_organizers"]
    text = ""
    width = 10 / max(len(list_logos), 1)
    for idx, path_logo in list_logos:
        text += "\\includegraphics[width=" + "%.2f" % width + "cm]{" + path_logo + "}"
        if idx < len(list_logos) - 1:
            text += "\\\\"
    filedata = filedata.replace("$LOGO_ORGANIZERS$", text)
    cfg.pop("path_logo_organizers", None)

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
        print(f"[ERROR] File failed: {fout}\nError: {er}")

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

    if not os.path.exists(path_output):
        os.mkdir(path_output)

    generate_certificate(
        name,
        "test",
        path_config=path_config,
        path_output=path_output,
        path_tex_template=path_tex_template,
    )

    generate_certificate(
        name,
        "test_work",
        work="Test Work",
        path_config=path_config,
        path_output=path_output,
        path_tex_template=path_tex_template,
    )

    generate_certificate(
        name,
        "test_plenary",
        work="Test Work",
        is_plenary_speaker=True,
        path_config=path_config,
        path_output=path_output,
        path_tex_template=path_tex_template,
    )


if __name__ == "__main__":
    typer.run(main)
