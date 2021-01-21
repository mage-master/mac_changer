# MAC CHANGER


A small python based tool intended to quickly change the MAC address of Linux Systems. 


## Execution
- 1. ```sudo python3 mac_changer.py```
- 2. ```sudo python3 mac_changer.py -i network_interface -m new_mac```
- I have coded the application to adapt to your way of execution so anyone of the above will work.
- replace *network_interface* with you Network Card Interface ID.
- replace *new_mac* to whatever MAC Address you wanna switch.
- *Use --help or -h for additional help while executing the program.*

## NOTE:
- On some Linux systems there maybe some unexpected errors
- Therefore use this format : **00:xx:xx:xx:xx:xx** where 00 always is at the first and then followed by your desired hex digits. 
- Python 3 is required to be installed on your system for the program to successfully execute.
- The additional software : **net-tools** can be easily installed from the terminal.
- Execute the script with root / superuser privileges.

## Bugs
- If you found any bugs report to mage-master@tutanota.com

### - Mage-Master
