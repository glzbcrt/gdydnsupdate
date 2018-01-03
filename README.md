# GoDaddy DNS Update &middot; [![GoDaddy DNS Update license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/glzbcrt/gdydnsupdate/blob/master/LICENSE)

Small utility I wrote to update my home external IP address so I could acess it remotely, even if the address did change.
As I use GoDaddy to host my DNS zone and it has a good API I wrote a simple Python script to update my external IP address.

I configured it to run as a systemd service in my Raspberry PI 3. It runs in a loop and at each 30 minutes if my external IP address did change it update my external host name.

This is my use case, but you might use it as a base to another use case where you will interact with GoDaddy DNS APIs.
Read the script. The constants you need to change are well documented.

Hope it helps someone! :)

