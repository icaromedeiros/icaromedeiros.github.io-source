#!/usr/bin/env bash
BRANCH=master
TARGET_REPO=icaromedeiros/icaromedeiros.github.io.git
PELICAN_OUTPUT_FOLDER=output
GOOGLE_WEBMASTER_HTML=googlec782d69d9cd6cf7f.html

echo "Compiling as make publish"
make publish
echo "Starting to deploy to Github Pages"
echo "Cloning target repo"
git clone --quiet --branch=$BRANCH git@github.com:$TARGET_REPO built_website > /dev/null
# google webmaster tools
cp $GOOGLE_WEBMASTER_HTML built_website
#go into directory and copy data we're interested in to that directory
cd built_website
rsync -rv --exclude=.git  ../$PELICAN_OUTPUT_FOLDER/* .
#add, commit and push files
git add -f .
DATE=`date "+%Y-%m-%d"`
echo "Commiting and pushing to target repo"
git commit -m "$DATE: update on Github Pages"
git push -fq origin $BRANCH > /dev/null
echo "Cleaning up.."
rm -rf built_website
echo "Deploy completed"
