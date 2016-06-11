# Git

## Credit where credit is due:
http://rogerdudler.github.io/git-guide/

## The entire "Pro Git" book is available for FREE online.  Go read it.
https://git-scm.com/book/en/v2

## Downloads:
https://git-scm.com/

## My favorite Git command:
`git log --graph --remotes --oneline --decorate`

## Ways To Create Repositories

### git init

- cd to your directory
- git init

### git clone

- git clone /path/to/repo
- git clone username@host:/path/to/repo

You do *not* need GitHub.  Let's leave that out of the mix for the time being, and focus solely on Git.

## Working Directory, Index, and HEAD

- Working directory is just that - your work in progress.
- Index is a "staging area" for commits to Git.
- HEAD is quite simply, a pointer to your last commit.

## Making A Change

The basic workflow is this:  Change a file (or files), add the change(s) to git, and commit the change(s).

- change file(s)
- git add file(s)
- git commit -m "My commit message"

### Good commit messages

http://chris.beams.io/posts/git-commit/

Good commit messages use the imperative mood in the subject line.

Examples of Imperative mood:

- Fix broken foo() function
- Merge Evan's branch
- Create new customer db table

## Pushing A Change

- git push origin <branch name>

Which can usually be shortned to:

- git push

This makes your change(s) available to others working from the same origin.

## Origin and remotes

Show which remotes you're working with
- git remote -v

To add remotes:
git remote add <shortname> <url>

Usually this is:
git remote add origin /path/to/repo
or
git remote add origin username@host:/path/to/repo

## fetching vs pulling

fetching retrieves changes from the remote, but does not update your code with the changes.  This lets you look at any changes, and decide if you want to update or not.

pulling retrieves changes from the remote, and updates your code automatically with what changed.  It's essentially a `git fetch && git merge origin/HEAD`

## Branching

- `git branch <branchname>`

## Checking out a branch

- `git checkout <branchname>`

## You can also create and check out a branch in one command

- `git checkout -b <branchname>`

## Merging

- `git checkout <my base branch>`
- `git merge <branch I want to merge in>`

## Other things I want to cover

- git stash
- rebasing (if we have time, and why it's a double-edged sword)


