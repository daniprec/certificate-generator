from certifigen.generator import generate_certificate

# Path to the list of participants
path_participants = "./participants.txt"
# Path where the certificates are stored
# Ensure you have created a folder with this name
path_output = "./certificates"

# Read the list
# We assume one name per line
with open(path_participants) as f:
    list_names = [s.rstrip("\n") for s in f.readlines()]

# Generate the certificates
for name in list_names:
    generate_certificate(name, path_output=path_output)
