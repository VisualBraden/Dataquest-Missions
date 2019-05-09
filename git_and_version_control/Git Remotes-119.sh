## 1. Introduction to Remote Repositories ##

/home/dq$ git clone /dataquest/user/git/chatbot

## 2. Making Changes to Cloned Repositories ##

/home/dq/chatbot$ git commit -m "Updated README.md"

## 3. Overview of the Master Branch ##

/home/dq/chatbot$ git status

## 4. Pushing Changes to the Remote ##

/home/dq/chatbot$ git push origin master

## 5. Viewing Individual Commits ##

/home/dq/chatbot$ git show 4bc2e9fdf94639ba7736f2051632ea4aef06fe42

## 6. Commits and the Working Directory ##

/home/dq/chatbot$ git diff 48fd bad7

## 7. Switching to a Specific Commit ##

/home/dq/chatbot$ git reset dd13

## 8. Pulling From a Remote Repo ##

/home/dq/chatbot$ git pull

## 9. Referring to the Most Recent Commit ##

/home/dq/chatbot$ git reset HEAD~1