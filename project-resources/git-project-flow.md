# Project Workflow on Git!

## Getting Started

1. One person make a new **public** repository on Github
  - Initialize with a `README`
  - Initialize with a `.gitignore` (most likely you'll be using Python)


2. Add your teammates as collaborators
  - Settings > Collaborators and Teams
  - Each other teammate accepts invitation sent to email


3. Add to your `.gitignore`:

```
# Logs and databases
*.log
*.sql
*.sqlite

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
*/.ipynb_checkpoints/*

# config file
config.py
```

4. Each teammate can clone down the repository! (No need to fork)
  - Each teammate creates a `config.py` for passwords/keys
  
5. If you want to work off the master branch, it's still important to regularly make commits with `git add .`, `git commit -m 'message'` and `git push`. A good practice is to always do a `git pull` before making changes.
  - If you run into conflicts, **read the error message** because it'll often tell you what you can do.
  - A common fix: do `git stash` followed by `git stash pop` (look it up!)

## Branches

Anyone can create branches! You can either create the branches remotely via Github or locally via command line.

#### Creating Branches on Github
1. In the repository on Github, where it says `Branch: master`, you can create your new branches.
2. To get the branches locally: `git fetch` then for **each** branch that you want locally, do `git checkout branch-name`.

#### Creating Branches Locally
1. `git checkout -b branch-name` to create the branch locally.
2. `git push -u origin branch-name` to push the branch to remote.


## While Working Separately...

Always work off your own branch!
1. `jupyter notebooks` do not merge well, so always work off different notebooks.
2. Python files (`~.py`) can be merged, so go ahead and work off the same file!
3. While on your own branch, you can save your work by doing the standard `git add .`, `git commit -m 'message'` and `git push`.
  - Doing `git push origin branch-name` does the same.
4. **[BONUS]** If you need a file from another branch, `git checkout other-branch-name --file-path-for-file-you-want`


## Putting Your Work Together

There are several ways to **merge branches**, but one of the easier/most _visual_ ways to do this is online on Github. The idea here is to get all updates onto **one** branch before pushing all the changes into the `master` branch. **Merge *ONE* branch at a time!**

1. Make sure all changes are pushed to each branch and decide which branch you want to merge all changes to. We'll call this your `base` branch.

2. On your Github repository, go to the tab `Pull requests` and click the green button `New pull request`. Here you can select which branch you want to merge to `base`, and click the green button `Create pull request`.

#### Merge Conflicts

- If you have unique files on each branch, the merge on these files should occur automatically.
- Again, because of the nature of raw `~.ipynb` files, merging is **highly discouraged**! A quick fix is to change the names of the files so they differ and track as different files.
- To solve merge conflicts on `~.py` files or `~.md` files, you can make edits on Github. Both versions will be combined into one, and you can delete the extra text on the files and make edits to create your final version.
- When you **submit** the pull request, you can then follow the steps to delete the now-redundant branch.


When you've put all new changes onto one branch, you can do the same to merge your final branch to `master` and your project is complete! Congratulations!
