# Github Actions Practice

## Description

This goal of this project is to practice using github actions to perform CI/CD.

_I am also using vim, (specifically neovim,) for the first time during this project!_

## Skills Learned

- Added .learn-gihub-actions.yml as first action from [github actions documentation]("https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions")
  - This action is triggered by pushes to the repo (including merged pull requests)
  - Has one job, "checks-bat-version" that:
    - runs on the latest version ubuntu runner
    - uses v4 of the checkout action to checkout repo files
    - uses an action to install node 14
    - uses npm to install `bats` software testing package
    - runs command that outputs bats software version
