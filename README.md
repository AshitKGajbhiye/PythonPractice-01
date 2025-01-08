# PythonPractice-01
Python basic coding practice

Installing Python and pip:
Windows

If you have not yet installed Python on your Windows OS, then download and install the latest Python3 installer from Python Downloads Page.

Download Python: 

Visit the [official Python website](https://www.python.org/downloads/) and download the latest version for Windows.
Install Python: Run the downloaded installer. Important: During the installation, make sure to select the option “Add Python to PATH”.

Make sure to check the box during installation which adds Python to PATH. Labeled something like Add Python 3.X to PATH
Once Python is installed, you should be able to open a command window, type python, hit ENTER, and see a Python prompt opened. Type quit() to exit it. You should also be able to run the command pip and see its options. If both of these work, then you are ready to go.

If you cannot run python or pip from a command prompt, you may need to add the Python installation directory path to the Windows PATH variable
The easiest way to do this is to find the new shortcut for Python in your start menu, right-click on the shortcut, and find the folder path for the python.exe file
For Python2, this will likely be something like C:\Python27
For Python3, this will likely be something like C:\Users\<USERNAME>\AppData\Local\Programs\Python\Python37
Open your Advanced System Settings window, navigate to the "Advanced" tab, and click the "Environment Variables" button

Create a new system variable:
Variable name: PYTHON_HOME
Variable value: <your_python_installation_directory>
Now modify the PATH system variable by appending the text ;%PYTHON_HOME%\;%PYTHON_HOME%;%PYTHON_HOME%\Scripts\ to the end of it.
Close out your windows, open a command window and make sure you can run the commands python and pip

Verify installation:
Open Command Prompt (search for “cmd” or “Command Prompt” and select the application).
Enter python --version and pip --version to check the installation.
