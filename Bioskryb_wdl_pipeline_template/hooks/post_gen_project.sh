#!/usr/bin/bash

set -e

wget https://github.com/broadinstitute/cromwell/releases/download/{{cookiecutter.womtool_version}}/womtool-{{cookiecutter.womtool_version}}.jar

git init

mv pre-commit .git/hooks
