# COMP8677-Networking-and-Data-Security-Final-Project

## Project Description
Final Project for COMP 8677 (Several Attacks using SEED lab)

## Local DNS Attack and Detection

Steps to Run the Project:
1. Build and Run the Docker Compose file
2. Get the docker container id of user, attacker and local DNS server with the help of ```dockps``` command
3. Open shell for these docker container ids using ```docksh <container_id>``` command
4. Run attack.py in the attacker shell to start the attack by executing the following command ```python3 attack.py <domain_name> <interface>```
5. User can check the IP address of the domain name whether it is spoofed or not by executing the following command ```python3 dns_local_attack_detection.py <domain_name>``` in the User shell

*Note: Everytime changing the IP address execute the ```rndc flush``` command in local DNS server shell to clear the local cache


## Reference

- For the implementation of local DNS attack, seedlab setup is used (https://seedsecuritylabs.org/Labs_20.04/Networking/DNS/DNS_Local/)
- I have made few changes in the docker-compose of the project, image_user/Dockerfile and volumes/attack.py
- The implmentation of volumes/dns_local_attack_detection.py is completely done by me
