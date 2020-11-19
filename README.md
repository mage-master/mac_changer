# MAC CHANGER

A small python to quickly change the MAC address of any linux machine. 
*The required additional software* - **net-tools** which you can easily install), this script requires root previlages to run.

Command : **sudo python3 mac_changer.py** (*or*) **sudo python3 mac_changer.py -i network_interface -m new_mac**.
*network_interface* is the network card name (example:**eth0**.
*new_mac* is where you specify MAC address that you want to change.

*Use --help or -h for the help message.* 

You can execute the script without or without the command line arguments, the script is coded to auto adpat to your imput.

**NOTE**: *On some Linux systems there maybe some unexpected errors, so enter the mac address starting with zeros: **00:xx:xx:xx:xx:xx**. 

*ps: Kindly be sane enough to input hexadecimal values in the x places, by this far you must already know that. Requires python 3.x to run*

**- mage-master**
