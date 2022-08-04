<!-- README template: https://github.com/othneildrew/Best-README-Template -->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/daniprec">
    <img src="img/ucadatalab.png" alt="Logo" width="auto" height="60">
  </a>

  <h3 align="center">CERTIFIGEN</h3>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#structure">Structure</a></li>
        <li><a href="#contributing">Contributing</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#install-dependencies">Install dependencies</a></li>
        <li><a href="#add-dependencies">Add dependencies</a></li>
      </ul>
    </li>
    <li>
      <a href="#how-to-use-certifigen">How to use CertifiGen</a>
      <ul>
        <li><a href="#modify-the-certificate">Modify the Certificate</a></li>
        <li><a href="#implementing-certifigen">Implementing CertifiGen</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## About the Project

CertifiGen is an automatic generator of certificates of assistance.

### Structure

The repository is structured into the following directories:

- `/certifigen`: where the python code is.


### Contributing

Conveniently, a set of workflows via Github actions are already installed:

- `black`: code formatting. We use this style of formatting.

In addition, all docstrings shall be be in the numpy format.

## Getting Started

### Install dependencies

There are two options, depending on whether you use conda or not:

- Conda: 
  ```
  conda env create -f environment.yml --force
  ```

- Pip: 
  ```
  pip install -r requirements.txt
  pip install -e .[dev]
  ```

you can also use `make install`.

The difference between conda and pip is that conda will create an isolated environment while pip will install all the dependencies in the current Python env. This might be a conda environment or any other Python env created by other tools. If you already have the dependencies installed, you can update it to reflect the last version of the packages in the `requirements.txt` with `pip-sync`. 

### Add dependencies

Add abstract dependency to `setup.py`. If neccessary, add version requirements but try to be as flexible as possible

- Update `requirements.txt`: `pip-compile --extra dev > requirements.txt`
- Update environment: `pip-sync`

## How to use CertifiGen

Once you have completed the [Getting started](#getting-started), you are ready to go!

First, activate the CertifiGen environment with the following command:

```
conda activate certifigen
```

You can do a test certificate by running:

```
python generate_certificate.py
```

The script will ask you to provide the participant name, its work and whether if they were a plenary speaker. Then, a sample certificate will be created inside the [certificates folder](./certificates/).

### Modify the certificate

All the certificate relevant information is stored in the [config file](./config.toml). You can open and modify this file with any text editor. Inside the file there is a brief description of what things can be changed in the certificate.

Remember that, to change the logos and signatures, you must provide new image files. We recommend to store them in the [images folder](./img/).

Once you are content with the new certificate information, try to generate one new sample certificate as explained above!

### Implementing CertifiGen

Once you have modified the [config file](./config.toml), running CertifiGen is fairly easy if you know some basic Python programming. This is how a code to generate one certificate would look like:

```python
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
```

Use the code above as template to do your own implementations. For instance, lets suppose that we have the list of participants in a txt file, and we want to generate a basic certificate for each one. Then we could do:

```python
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
```

You can find these and other use cases in the [examples](./examples/) folder.

## Contact

Daniel Precioso - [daniprec](https://github.com/daniprec/) - daniel.precioso@uca.es

Project link: [https://github.com/daniprec/certificate-generator](https://github.com/daniprec/certificate-generator)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/daniprec/certificate-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/daniprec/certificate-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/daniprec/certificate-generator.svg?style=for-the-badge
[forks-url]: https://github.com/daniprec/certificate-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/daniprec/certificate-generator.svg?style=for-the-badge
[stars-url]: https://github.com/daniprec/certificate-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/daniprec/certificate-generator.svg?style=for-the-badge
[issues-url]: https://github.com/daniprec/certificate-generator/issues
