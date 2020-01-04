# AutoProjectCreation on Windows
## Origin
I saw Kalle Halden make this project for Mac using Selenium and I wanted to try it but using just Github. His video: https://www.youtube.com/watch?v=7Y8Ppin12r4
## How to install it
Make sure you have Python installed first


Go to your CMD and navigate to the folder where you want to clone this and copy the commands:
```bash
git clone https://github.com/LittleHaku/AutoProjectCreation.git
cd AutoProjectCreation
pip install PyGithub
```
Then edit the file **create.bat** and **create.py** where it is said with comments

**MOST DIFFICULT**: Here follow me step by step.
1. Type **env** to inside the windows search and a window with properties must pop up.
2. In the top window click on **PATH** and edit it.
3. Click **New** and paste the location where the batch is, example: "G:\Proyectos\AutoProjectCreation\batch" and accept that.
4. Go back to the window where PATH and more things are and press **New...** and create a variable with the name **GIT_USER** and your Github username.
5. Repeat the step 4 but this time create a variable with the name **GIT_PASS** and your Github password.

## How to use it
Use the CMD and type:
```bash
create ProjectName private/public
```
+ **ProjectName**: Here write your project **WITHOUT** spaces.
+ **private/public**: Here state if you want your Github repository to be private or public.