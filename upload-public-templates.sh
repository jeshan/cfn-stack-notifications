#!/usr/bin/env bash

aws s3 cp --profile jeshanco templates/template.yaml s3://jeshan-oss-public-files/cfn-stack-notifications-template.yaml
aws s3 cp --profile jeshanco templates/deployment-pipeline.yaml s3://jeshan-oss-public-files/cfn-stack-notifications-deployment-pipeline-template.yaml
