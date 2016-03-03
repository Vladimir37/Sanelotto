# Sanelotto
<image src='https://raw.githubusercontent.com/Vladimir37/Sanelotto_site/master/src/files/logos/logo_mid.png' alt='logo1' style='vertical-align: middle;'>

Sanelotto developed for fast and simple deploy applications to server.

Sanelotto is suitable for any languages and any frameworks. Configuring is extremely simple - only need to change JSON configuration files and enter the desired commands on the desired language.

After creating project you will get two directories - for local machine (usually virtual machine on Continuous Integration service) and for server. During the update repository on GitHub local part make a SSH connection with server part and update project on server. 

## Dependencies
* Python 3
* Git

## Features
* SSH connection through SSH-key or login/password
* Four types custom commands: before connection, after first downloading, after updating, after first downloading and updating
* Automatically overwrinig chosen files
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
