# 0x06. Star Wars API
Algorithm
API
JavaScript

## Requirements

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-  Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
-   All your files must be executable
-   The length of your files will be tested using `wc`
-   You are not allowed to use `var`

## Tasks

### 0. Star Wars Characters

Write a script that prints all characters of a Star Wars movie:

-   The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”
-   Display one character name per line **in the same order as the “characters” list in the `/films/` endpoint**
-   You must use the [Star wars API](`https://swapi-api.alx-tools.com/documentation`)
-  You must use the `request` module

```sh
guillaume@ubuntu:~/0x14$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```