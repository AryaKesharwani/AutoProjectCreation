::Change this to where you have "create.py"
cd G:\Proyectos\AutoProjectCreation

python create.py %1 %2

::Change this to where you want to save your projects
cd G:\Proyectos\%1

git init


::Change the LittleHaku for your own user name
git remote rm origin
git remote add origin https://github.com/LittleHaku/%1.git

echo #%1 > README.md

git add .
git commit -m "initial commit"
git push -u origin master

code .