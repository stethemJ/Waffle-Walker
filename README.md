###  Author: Jack Stethem
###  Date: 12/18/2024
###  Email: stethem.5@osu.edu


**INSTRUCTIONS FOR CREATING A BRANCH AND DOING WORK**
You should create a branch each time you want to do a bit of work on the game. Here are the exact steps you need to take to do this.

1. Decide the task you are working on.
2. Change to the directory in which this repo is located in your local space.

3. git checkout main
4. git pull origin main #Steps 3 and 4 ensure that you are starting from the main branch, and have updated the main branch to include all changes from other contributors before you begin your work

5. git checkout -b branch-name #You change the branch name to describe your task.

6. Now you can make your edits #This is when you write your code. You can make a new directory, add a text file, write a script to make plots in an existing directory, or anything which is part of
   your analysis. Please do not save large files and plots within the directory of this repository, rather keep them on the shared group space.

8. git status #This checks which files have been made during your work.

9. git add . #This stages all your files to be added to the repository
10. git commit -m "message about your changes" #This is where you actively add your files to the repository with a descriptive message about your work. Please include the "" when running this command
11. git push origin branch-name #This pushes your branch and additions to the main branch

12. Now someone needs to go to the gitHub repository on the browser and accept the push and merge. Anyone can do this as long as they have admin access.

_Nota Bene_ - If you have been working on your branch in multiple instances (i.e. you work on your analysis one day then come back the next) here is what you should do upon load up.
1. Change to the directory in which this repo is located in your local space.
2. git checkout <branch-name>
3. git fetch origin
4. git merge origin/main

This ensures that you are working on an updated version of your branch. Once finished you complete steps 8-12 as normal.

Now for a first test run, try the task of creating a text file in the /examples directory in a similar fashion to me. Use the steps above to create a branch for completing this task and let me know if you have any questions!
