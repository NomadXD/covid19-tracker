

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/NomadXD/covid19-tracker.git">
    <img src="static/assets/img/virus.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Covid19-tracker</h3>

  <p align="center">
   Covid 19 Analytics Dashboard for Sri Lanka
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="#">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)




<!-- ABOUT THE PROJECT -->
## About The Project
**Covid-19 tracker is an Analytics Dashboard for the covid 19 cases reported in Sri Lanka. It uses Uber’s Hexagonal Hierarchical Spatial Index library to cluster and represent the cases based on the location**
[![Product Name Screen Shot]product-screenshot]

The repository contain the project files for the Covid19-tracker dashboard. This is just a one night project done solely for the purpose of fun.
All the API functions are implemented in the ***app.py*** file. ***index.html*** file in the templates folder is the view that is rendered. ***static/html/map.html*** is a dynamically generated map that contains the clusters. Clustering is done by Uber H3 library. Firebase is used as the database.     

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Firebase](https://firebase.google.com/)
* [Uber H3](https://eng.uber.com/h3/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites


* Firebase account
* Python3
* Flask
* Folium
* Numpy
* Pandas
* H3

### Installation
 
1. Clone the repo 
```sh
git clone https://github.com/NomadXD/covid19-tracker.git
cd covid19-tracker
```
2. Install the required packages with pip or conda
```sh
pip install <package name>
```
3. Start the server with flask run. (from the project root)
```sh
flask run
```
<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/github_username/repo/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Lahiru Udayanga - lahiru97udayanga@gmail.com







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: static/assets/img/cover.png

