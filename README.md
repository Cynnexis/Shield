# Shield - Network Guardian
Shield is a python script which can change your MAC address very quickly, by setting down/up the network interface automatically. The real advantage of using Shield is the MAC address prefix (the three hexadecimal number at the beginning of the MAC address) use the [macchanger](https://github.com/alobbs/macchanger) database to create a MAC address just like it was made by a real producer, to make your fake MAC address as real as possible.

## Downloading and installation:
You just have to download the files ```mac_producer.list``` and ```shield.py```. The file ```mac_producer``` is not necessary. Actually, ```mac_producer.list``` and ```mac_producer``` are the same file, except ```mac_producer.list``` is compiled by Pickle library. ```shield.py``` detect automatically if ```mac_producer.list``` exists. If it does not, it will try to compile the database from ```mac_producer```. But if there is neither ```mac_producer.list``` nor ```mac_producer```, the script cannot do anything and will exit. In other word, you just have to make sur there is either  ```mac_producer.list``` or ```mac_producer``` in the same directoy of ```shield.py```.

## Usage:
shield.py [change | reset] INTERFACE

## Description:
change INTERFACE    Change INTERFACE mac address.<br/>
reset  INTERFACE    Reset INTERFACE mac address.

## Examples:
```bash
# Assuming wlan0 as network interface
shield.py change wlan0 # Change wlan0 mac address.
shield.py reset wlan0  # Reset wlan0 mac address.
```

## See also:
```bash
ifconfig (8)
```

## Author:
Valentin Berger <[valentin.berger38@gmail.com](mailto:valentin.berger38@gmail.com)>

### Note:
As a french student who try to learn english, I think there is a LOT of mistake in those texts (also in the source code). So, you're welcome to warn me about it if you find one of them. Just let me know ;)
