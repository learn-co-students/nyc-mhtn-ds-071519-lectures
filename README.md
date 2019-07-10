# Lecture Notes for nyc-mhtn-ds-071519 :floppy_disk:

## To update a local repo after forking and cloning

### If you have set the remote skip to step :two:

1. Add the learn-co lecture notes repo as the remote, **this step only happens once**
```
git remote add upstream https://github.com/learn-co-students/nyc-mhtn-ds-071519-lectures.git
```

2. Check the remote is set and your lecture notes repo is correct.
You should see your forked repo after **origin**, and the learn-co-students repo after **upstream**

```
git remote -v
```

3. Update the changes from the upstream learn-co lecture notes repo
```
git fetch upstream
```

4. Check that the master branch is selected
```
git branch
```

5. Merge the new changes from the upstream learn-co lecture notes repo, with a commit message
```
git merge upstream/master -m 'what you updated'
```

6. Push the changes to the forked lecture repo :raised_hands:
```
git push
```
