from certifigen.generator import generate_certificate

# Name of the participant
name_of_participant = "Daniel Precioso"
# Filename of the certificate
filename = "daniel"  # The output will be "daniel.pdf"
# Title of the work presented by this partipant (if any)
work_title = "CertifiGen"
# Was the participant a plenary speaker
is_plenary_speaker = True
# Path to the config file (see section above)
# You usually wont need to provide this parameter
path_config = "./config.toml"
# Path where the certificates are stored
# Ensure you have created a folder with this name
path_output = "./certificates"
# Path to the LaTeX template
# You usually wont need to provide this parameter
path_tex_template = "./certifigen/main.tex"

# Generate the certificate
generate_certificate(
    name_of_participant,
    fout=filename,
    work=work_title,
    is_plenary_speaker=is_plenary_speaker,
    path_config=path_config,
    path_output=path_output,
    path_tex_template=path_tex_template,
)
