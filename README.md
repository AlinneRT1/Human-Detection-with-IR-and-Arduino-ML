<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://user-images.githubusercontent.com/80778103/111392388-79129c80-8684-11eb-815e-9d02912d8949.png" alt="Spatium Logo" width="384" height="102">
  </a>

  <h3 align="center">README-Documentation</h3>

  <p align="center">
    A README section to explain our project!
    <br />
    <br />
    ·
    <a href="https://docs.google.com/presentation/d/1KfYwGe0AA0E7Ch4aedEjBdQMeWxgiPScIx-qY8ihDGc/edit?usp=sharing">Detailed Project Directions Project Binder</a>
    ·
    <a href="https://docs.google.com/presentation/d/11XmQhKTzX6NftyJUHzmJs5xDNz7pBZND4y6fTvALAWo/edit?usp=sharing">YWPN Presentation</a>
     ·
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#code images">Code Images</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<p align="center">
    <img src="https://youngwomensprep.org/wp-content/uploads/2021/01/STEAM-Challenge-logo-.png" alt="YWPN Logo" width="384" height="102">
  </a>
   <br />
This project was completed for a Network STEAM Challenge. This code is for our developing model, rather thatn relting on infrared signals like our prototype this implements machine learning to detect humans and their distance. This would be a more practical solution for individual use. Like our prototype, We hope that this helps maintain individuals socially diatanced. Our maximum accuracy reached with only 200 images was 92%, relativley high for a small sample size.

* Detects Humans and their distance using heat signatures
* Can be used independently
* Uses tiny ML with the Arduino 33 BLE sense making it a small portable solution

### Built With

Required materials to implement this model are...
* Arduino 33 BLE Sense
* Adafruit AMG8833 8x8 Thermal Camera Sensor
* 9 v battery
* Rocker Switch
* Piezo Buzzer
* .96" OLED display ![Picture3]()

<p align="center">
    <img src="https://user-images.githubusercontent.com/80778103/111673724-42a26200-87e9-11eb-811c-1e9bbb390229.png" alt="Diagram" width="500" height="237">
  </a>


<!-- GETTING STARTED -->
## Getting Started
We recommend installing all of this software prior to beginning
* Arduino IDE
* Thonny or other python IDE
* [Netron (For vizualizing your Neural Network](https://github.com/lutzroeder/netron/releases/tag/v4.8.2)
* Visual Studios, or some place to open C++ header files
* Jupyter Notebooks or Google Colab

### Prerequisites

Install all required libraries and their dependencies.
You can do this using the command prompt and the pip installer
* numpy
* Pillow
* SciPy
* Math
* os
* tensorflow

  ```sh
  pip install numpy
  pip install Pillow
  pip install scipy
  pip install tensor2tensor
  ```

### Code images
This is a gallery of what this code does and how it looks. For more detailed directions visit the procedure section of our [binder](https://docs.google.com/presentation/d/1KfYwGe0AA0E7Ch4aedEjBdQMeWxgiPScIx-qY8ihDGc/edit#slide=id.gc84627ac26_0_32).

<p align="center">
    <img src="https://user-images.githubusercontent.com/80778103/111675350-053ed400-87eb-11eb-9b0c-ca08e73d7e9e.jpg" alt="Diagram" width="300" height="219">
  </a>
<p align="center">
    <img src="https://user-images.githubusercontent.com/80778103/111676432-2522c780-87ec-11eb-8f9a-446a2885f6af.jpg" alt="Diagram" width="400" height="281">
  </a>
<p align="center">
    <img src="https://user-images.githubusercontent.com/80778103/111676442-281db800-87ec-11eb-974e-5e4b2275f6ad.jpg" alt="Diagram" width="400" height="390">
  </a>
<p align="center">
    <img src="https://user-images.githubusercontent.com/80778103/111676451-2bb13f00-87ec-11eb-927b-2f8271e7b5c6.jpg" alt="Diagram" width="400" height="405">
  </a>
 <p align="center">
    <img src="https://user-images.githubusercontent.com/80778103/111676502-3a97f180-87ec-11eb-8f0c-c78a53216a70.jpg" alt="Diagram" width="400" height="292">
  </a>
  <p align="center">
    <img src="https://user-images.githubusercontent.com/80778103/111676519-3d92e200-87ec-11eb-8a5e-4683bdbddb4c.jpg" alt="Diagram" width="400" height="277">
  </a>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/AlinneRT1/Human-Detection-with-IR-and-Arduino-ML](https://github.com/AlinneRT1/Human-Detection-with-IR-and-Arduino-ML)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Blacklight UTILS Library](https://github.com/BlackLight/imgdetect-utils)
* [Fabio Manganiello's Human Detection with Rasberry Pi](https://blog.platypush.tech/article/Detect-people-with-a-RaspberryPi-a-thermal-camera-Platypush-and-a-pinch-of-machine-learning)
* [Adafruit Raw IR Values LIbrary](http://www.adafruit.com/products/3538)
* [Adafruit amg8833-8x8 Directions](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor/python-circuitpython)
* [Digikey SHAWNHYMEL's Tiny ML code and Directions](https://www.digikey.com/en/maker/projects/intro-to-tinyml-part-1-training-a-model-for-arduino-in-tensorflow/8f1fc8c0b83d417ab521c48864d2a8ec)
* [READ.ME Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
