# PyRemote
Python script to machine remote control

## About
Very simple script to control personal machine with Twitter account.

## Function
`d&e` - Download & Execute
- `d&e||https://example.com/bash.sh`

`o_s` - Open Site, just send GET request to site
- `o_s||https://www.google.com`

`de&agr` - Download&Execute with agrs
- `d&e||https://example.com/bash.sh||-a 100 -b 90 -c -`

`sys` - run command in system console
- `sys||echo "passsword1"|sudo -S apt-get update&&sudo apt-get upgrade`
