# Sanelotto
<image src='https://raw.githubusercontent.com/Vladimir37/Sanelotto_site/master/src/files/logos/logo_mid.png' alt='logo1' style='vertical-align: middle;'>

<a href='https://semaphoreci.com/vladimir37/sanelotto'> <img src='https://semaphoreci.com/api/v1/vladimir37/sanelotto/branches/master/shields_badge.svg' alt='Build Status'></a>
<a href="https://badge.fury.io/py/sanelotto"><img src="https://badge.fury.io/py/sanelotto.svg" alt="PyPI version"></a>

Sanelotto is developed for fast and easy application deployment on the server.

Sanelotto is suitable for any frameworks and languages. The setup is quite easy - you need to simply edit the JSON configuration files and enter any comands on any desired language.

After creating the project you will get two directories, one for the local machine (usually a virtual machine on Continuous Integration service) and one for the server. The local part connects to the server through SHH after updating the repository on GitHub. After that, the local part updates the project on the server.

## Dependencies
* Python 3
* Git

## Features
* SSH connection through SSH-key or login/password
* Four types of custom commands: before the connection, after the first download, after updating, after the first downloading and updating
* Automatic overwriting of selected files
* Optional detailed logging

## Benefits
* Simple and fast
* Multilanguage
* Full Open Source
* Crossplatform
* For any CI services
* Highly customizable through configuration files

## Documentation
* [Full documentation](http://sanelotto.info/)
* [Documentation source](https://github.com/Vladimir37/Sanelotto_site)
