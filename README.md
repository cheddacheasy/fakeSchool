<div id="top"></div>




<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Fake School (In Progress) </h3>

  <p align="center">
    A minimalistic Python library to generate fake student data
    <br />
    <!--
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


When I would work on some projects sometimes I found that I needed fake data that would be centered around a student demographic. When I would scroll through Github I found myself finding randome data generators for personal information; if I did find a random generator, it was in a langauge I was not familar with or it was not in Python. So in short I did not find something that could solve my data problem and often I would be orchestrating different random generators and spending more time create random generating data then working on the bigger problem that needed rando data. Now that I have time, I decided to create a randome student generator.

I do understand that you cannot use a Swiss army knife for every problem, especially when it comes to fake data. However, having a fake data template that you can create and manipulate to fit your needs can be very valuable. So that is why I created fake school. As always please feel free to make suggestion for changes by forking this repo and creating a pull request or opening an issue.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [pandas](https://pandas.pydata.org/)
* [names](https://github.com/treyhunner/names)
* [Faker](https://faker.readthedocs.io/en/master/)


<p align="right">(<a href="#top">back to top</a>)</p>




## Compatibility
Fake School only supports Python 3.10 and above for the time being. If your system does not support Python 3.10, my recommendation would be to use Poetry and pyenv to setup a vrtiual environemnt to use this package inside of your project directory. 

<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

The following commands should be able to give you the most up to date of all the prerquisites.
* pandas
  ```sh
  pip install pandas
  ```
* names
  ```sh
  pip install names
  ```
* Faker
  ```sh
  pip install Faker
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo into your project folder
   ```sh
   git clone https://github.com/cheddacheasy/fakeSchool.git
   ```
2. Just make sure to include the module in the top of your project file. Hop to the usage section to see what is available.
  ```sh
  # my preference when using this module
  import student as st
  ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
* Object creation

    There are two different type of objects that you can create with fake school. You can create a student object that contain information that revolves around academia portion associated with a student. For example, you would The other type of student object has data centered around the administration portion associated with a student. For example you would see the students name, Social Security Id, Home address.
    
    
  * admininstrative student object

  ```sh
   import student as st
   
   # this will generate a random student that will be associated with the administration 
   person1 = st.Person()
   
   # this will produce the administration portion associated with the student object
   person1.person_info()
    
   ```
  * academia student object
   ```sh
     import student as st

     # this will generate a random student that will be associated with the academia 
     student1 = st.Student()

     # this will produce the academia portion associated with the student object
     person1.college_info()

     ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add Methods to README
- [ ] Add docstrings to methods and functions
- [ ] Add information about testing 
- [ ] Add CSV compatibility
- [ ] Clean up Acknowldgement section
- [ ] Create PyPi project

See the [open issues]([https://github.com/cheddacheasy/fakeSchool.git/issues]) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b fakeSchool/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin fakeSchool/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Larry White Jr. - larry.l.white99@gmail.com

Project Link: [https://github.com/cheddacheasy/fakeSchool.git](https://github.com/cheddacheasy/fakeSchool.git)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)
-->

<p align="right">(<a href="#top">back to top</a>)</p>



