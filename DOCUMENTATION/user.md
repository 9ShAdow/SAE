<h1> Doc User</h1>


## INTRODUCTION

This project goal is to communicate a client and one or more servers through a GUI.
In the following doc i will explain how you can do the same thing 


1. [__What/How intall the the packages ?__](#What/How-intall-the-the-packages)
2. [__How to start ?__](#How-to-start-?)
3. [__How to use the GUI ?__](#How-to-use-the-GUI-?)




## What/How intall the the packages 




<pre>after downloading my folder open a terminal and intall the following pacages: (make sure you have an up-to-date version of python)</pre>



```pip install netifaces     /    pip3 install netifaces```    
```pip install socket     /    pip3 install socket```   
```pip install threading     /    pip3 install threading```     
```pip install time     /    pip3 install time```    
```pip install os     /    pip3 install os```    
```pip install sys     /    pip3 install sys```   
```pip install psutil     /    pip3 install psutil``` ( pour afficher les perfomances du système )       
```pip install platform     /    pip3 install platform```(pour afficher l'OS)  
```pip install pyqt6     /    pip3 install pyqt6```   

##

## How to start ?

The first thing to do is run the server1.py file,
once you have run it file you can start the client.py.

You must run this two file with python or python3.


# Now we are ready to start!

## How to use the GUI ?
A GUI will appear 

The user can enter the following requests:



   <pre> 
    - OS: asks for the OS and the type of OS for example MacOS Darwin or Linux Ubuntu 21.4
    - RAM: total memory, used memory and remaining free memory
    - CPU: CPU usage
    - IP: IP address
    - Name: machine name
    - Send commands to machine servers:
        - Connection information: IP, machine name
        - Kill: kills the server
- In addition, the interface will allow to send commands given by
  the user, for example:
 
    - DOS:dir
    - DOS: mkdir foo
    - Linux:ls -la
    - python --version
    -ping </pre>

The button on the GUI will return some of this request to the user 



<pre>TEFANG Ivan RT222 <pre>
