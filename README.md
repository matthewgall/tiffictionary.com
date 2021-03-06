# tiffictionary.com

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/matthewgall/tiffictionary.com/build?color=db422a&logoColor=FFFFFF&style=for-the-badge)
![Docker Pulls](https://img.shields.io/docker/pulls/matthewgall/tiffictionary.com?color=db422a&logoColor=2a6bdb&style=for-the-badge)
![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/matthewgall/tiffictionary.com?color=db422a&logoColor=2a6bdb&style=for-the-badge)
![Docker Stars](https://img.shields.io/docker/stars/matthewgall/tiffictionary.com?color=db422a&logoColor=2a6bdb&style=for-the-badge)
![Docker Image Version (latest by date)](https://img.shields.io/docker/v/matthewgall/tiffictionary.com?color=db422a&logoColor=2a6bdb&style=for-the-badge)

American? Confused by British English? Introducing the Tiff-ictionary! Input the word, get a definition!

## Introducing tiffictionary.com
Powered by Python and bottle, tiffictionary.com is quick and simple to deploy, using all the power of [Docker](https://docker.io) you can be up and running in one command!

## Deploying
Deploying tiffictionary.com is easy using Docker:

    docker run -p 80:5000 matthewgall/tiffictionary.com

Honestly, that simple (and none of that one line wget direct to your terminal)

## Features

### /version
Returns the current running version of tiffictionary.com from the released commit hash

    $ curl https://tiffictionary.com/version
    a54fda84993b524288b9597131f8d3aec3945e06


## Licence

    The MIT License (MIT)

    Copyright (c) 2020 Matthew Gall

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.