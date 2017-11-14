# Contribution Guidelines
1. For each program a directory should be there with two files `<program_name.py>` and `<tests.py>`
2. PR should be made from new branch only, check [How To Create PR](#how-to-create-pr)
3. Test file should pass all the build(s) from travis-ci, check [this](https://github.com/prognite/python/blob/master/BUILD_GUIDE.md) if you have doubt related to testing

# How To Create PR
1. Create new branch
```
git checkout -b <topic-branch>
```
2. After creating your code and test file, add to staging area
```
git add .
```
3. Commit the changes
```
git commit -m "relevant message"
```
4. Push to HEAD (current branch)
```
git push origin HEAD
```
5. Open repo on your browser -> compare branch and create pull request
