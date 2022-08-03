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

  <h3 align="center">CERTIFICATE OF ASSISTANCE GENERATOR</h3>
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
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## About the Project

Automatic generator of certificates of assistance.

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
