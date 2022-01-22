
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/waters262/JupyterCloud">
    <img src="images/OCI_Comp_4K_HQ_thumb.gif" alt="Logo" width="200" height="100">
  </a>

<h3 align="center">Jupyter Cloud Project</h3>

  <p align="center">
    This project will use Jupyter Notebooks (python) to explore the internals of the OCI Cloud Environment using the OCI Python SDK (mostly) and some CLI as needed/convienent.
    <br />
    <a href="https://github.com/waters262/JupyterCloud"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://youtu.be/5VtN99HX3IQ">View Demo Video</a>
    ·
    <a href="https://github.com/waters262/JupyterCloud/issues">Report Bug</a>
    ·
    <a href="https://github.com/waters262/JupyterCloud/issues">Request Feature</a>
  </p>
</div>


# Introduction

   <p>Jupyter Notebooks developed for Cloud Environments - current focus is on Oracle Cloud (OCI):</p>
   <p> The Jupyter Notebooks in this project gives anyone who wants to do cool stuff fast in the Cloud the means to do so by leveraging the knowlegde of a skilled Cloud developer.  Thereby giving useful insight into Cloud Environments (namely OCI) in a "real world" context.</p>

## Disclaimer
<p>
The opinions and techniques used in this repository are those of the author/contibuters and in no way meant to refelect the best practices or opinions of Oracle Corporation and will also not be supported by Oracle.
  </p>

## Featured Notebooks

### Authentication
   <p>This Notebook can best be used to authenticate to OCI tenancy's that require multi-factor authentication of any form. Once authenticated, there are cells in the notebook to quickly refresh your session, which is nice to have since session typically have a time limit. There is also a repeating cell which will keep you session alive for hours, as needed.</p>

### Bastion Ops
   <p> This Notebook is very useful in creating Bastion Session for both Managed Server and Port Forwarding Servers. After a few configurations are made, sessions that ssh strings that are created have all the information needed to simply copy and paste to your xterm access tool. Port Forwarding which provides tunneling to VM servers is also included.</p>

### Terraform Ops
   <p>This Notebook provides an easy way to quickly create Terraform Stack, Jobs and Templates. Specifically designed for serverless function environments, a cell tool is in this notebook that will get the State of a Stack and transform the output to an organized report format. In addition, the tool will create a Resource Map that can used in a Metric Monitoring notebook this is currently being planned.
  </p>



<!-- ABOUT THE PROJECT -->
## About The Project and Background

<p>I started using Jupyter Notebook for Python development several years ago and found that it gave me enjoyment while coding in Python and so became my development platform of choice.</p>

See Roadmap below for what is ready for use and what is now in progress

### Built With

* [Jupyter Notebook](https://anaconda.com/)
* [oracle-cli](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm)
* [SDK for Python](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/pythonsdk.htm)
* [Mathjax](https://mathjax.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

The obvious requirement for this getting started is to have Jupyter Notebooks installed on your computer.<br>
I strongly recommend using Anaconda 

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
TBD
<!-- ROADMAP -->
## Roadmap

- [x] OCI Authentication
- [x] OCI Bastion Session Manager
- [x] Terraform for Functions
- [ ] Functions Monitor


See the [open issues](https://github.com/waters262/JupyterCloud/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

## Insights
<p>This series of Jupyter Notebooks is meant to provide a user with insight into Cloud Environments (namely OCI) in a "real world" context.</p>
<p>For example, a realistic way of authenticating into most major corporate cloud environment is by using Multi-Factor Authentication which requires some kind of physical interaction in order to gain access.  This can be overcome by using Instance Principals, however, an Instance Principal requires that you operate on a Cloud VM, which is inconvienent and requires much time to set up.  It is far better to use ones own desktop or laptop.</p>
<p>So that these notebooks can operate in any environment, an Authentication notebook is made available to easily authenticate to your tenancy and stay authenticated for as long as you like.  See the OCI_Auth_Multi_Factor notebook for furhter details.</p>

### Bastion
>For security, company's that use the Cloud environments will not allow direct access to Virtual Machines to developers, admins, etc..
>Instead they provide Bastion Services for access to VM's. This is good practice, however, it forces users to go through a process to obtain time limited tokens for access. >For users who must access frequently, such as developer, the process can become cumbersome and tedious.
>The requested notebook will facilitate the process by using the Python SDK to create a Bastion Session and an 'ssh' connection string from which to copy, then paste to >your favorite terminal access tool like MobaXterm.

## References

**Reference Document Links:**<br>
[OCI CLI Docs](https://docs.cloud.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html)<br>
[Python SDK docs](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/landing.html)<br>
[Core Services](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/core.html)<br>
   <br>
**Getting Started References**<br>
[Learn OCI CLI  ](https://github.com/oracle/learning-library/tree/master/oci-library/DevOps/OCI_CLI)<br>
[Learn DevOps Resource Manager](https://github.com/oracle/learning-library/tree/master/oci-library/DevOps/Resource_Manager)<br>
[Learn DevOps Terraform](https://github.com/oracle/learning-library/tree/master/oci-library/DevOps/Terraform)<br>
[Example Python SDK - showoci](https://github.com/oracle/oci-python-sdk/tree/master/examples/showoci)<br>
[Learn DevOps Container Registry  ](https://github.com/oracle/learning-library/tree/master/oci-library/DevOps/Container_Registry) <br>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Kevin Waters - [@waters262](https://twitter.com/waters262) - waters262@gmail.com

Project Link: [https://github.com/waters262/JupyterCloud](https://github.com/waters262/JupyterCloud)

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/waters262/JupyterCloud.svg?style=for-the-badge
[contributors-url]: https://github.com/waters262/JupyterCloud/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/waters262/JupyterCloud.svg?style=for-the-badge
[forks-url]: https://github.com/waters262/JupyterCloud/network/members
[stars-shield]: https://img.shields.io/github/stars/waters262/JupyterCloud.svg?style=for-the-badge
[stars-url]: https://github.com/waters262/JupyterCloud/stargazers
[issues-shield]: https://img.shields.io/github/issues/waters262/JupyterCloud.svg?style=for-the-badge
[issues-url]: https://github.com/waters262/JupyterCloud/issues
[license-shield]: https://img.shields.io/github/license/waters262/JupyterCloud.svg?style=for-the-badge
[license-url]: https://github.com/waters262/JupyterCloud/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kevin-waters-b47a8424
[product-screenshot]: images/screenshot.png
