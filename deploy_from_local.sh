export TRAVIS_PULL_REQUEST=false
export GH_TOKEN=`cat github_token`
export TRAVIS_BUILD_NUMBER=LOCAL
source deploy.sh
cd ..
rm -fr built_website
