BUMP_TYPE=$1
MESSAGE=$2

set -e

bumpversion  --allow-dirty $BUMP_TYPE
git add .
git commit -m "$2"
git push origin
