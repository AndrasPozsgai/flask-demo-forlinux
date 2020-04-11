#-------static-flask-demo on Ubuntu-----------#


# open terminal

Ctrl+T


# create project folder

mkdir project
cd project

*Short hand for Flask setup*
# updating the package list

      $sudo apt update
      
# Install pyton current version  in terminal: 
      $sudo apt-get install python             
      $--python version                           # check python version
# install pip
      
      $sudo apt install python3-pip               # acording to current python version 

# install virtualenv (virtualenvoitment with pip)
      
      $pip --version
      
      $pip3 --version                             # version check


#  intall virtualenv with pip  (if you have py3 version install pip3)
      
      $sudo pip install virtualenv
      
      $sudo pip3 install virtualenv 
      
      
      
# Create a virtual envoirment
      
      $virtualenv venv
      
      $python3 -m venv myenv
      
# You able choise the Python intrepeter

      $virtualenv -p /usr/bin/python2.7 venv       # for 2.x Python version
      
      $virtualenv -p python3 myenv                 # for 3.+ version
      
  

# start virtualenv (terminal)

      $source venv/bin/activate




