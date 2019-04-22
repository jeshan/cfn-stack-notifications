#!/usr/bin/env bash
set -e

BRANCH=`git rev-parse --abbrev-ref HEAD`
echo "On branch ${BRANCH}"

aws s3 sync --delete --exclude "*" --include "config/*" --exclude "config/config.yaml" \
  --exclude "config/dev/*" --exclude "config/deployment/*" \
  . s3://jeshan-oss-private-files/github.com/jeshan/cfn-stack-notifications/${BRANCH}/
