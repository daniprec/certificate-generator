import os
from certifigen.generator import generate_certificate
import typer


def main(
    path_config: str = "./config.toml",
    path_output: str = "certificates",
    path_tex_template: str = "./certifigen/main.tex",
):
    # Create the "certificates" folder
    if not os.path.exists(path_output):
        os.mkdir(path_output)

    # Ask the user for input
    name = input("Name of the participant: ")
    work = input("Title of the work (if none press ENTER): ")
    if len(work) > 0:
        is_plenary_speaker = input("Is the participant a plenary speaker? (y/n): ")
        if is_plenary_speaker == "y":
            is_plenary_speaker = True
        else:
            is_plenary_speaker = False
    else:
        work = None
        is_plenary_speaker = False

    # Generate the certificate
    generate_certificate(
        name,
        name,
        work=work,
        is_plenary_speaker=is_plenary_speaker,
        path_config=path_config,
        path_output=path_output,
        path_tex_template=path_tex_template,
    )


if __name__ == "__main__":
    typer.run(main)
