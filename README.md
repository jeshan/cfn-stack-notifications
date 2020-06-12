# cfn-stack-notifications

Sets up an SNS topic for all your stacks in all regions.

This will be useful when you want to track deployments. The SNS topics can relay messages to many destinations, including AWS Lambda. This means you can subscribe a function to the topic and send deployment events to your chatbot. (see [this project](https://github.com/jeshan/cfn-failures-to-telegram) for an example that sends cloudformation failures to telegram)

If needed, you can create a virtual env with `pipenv install`

This includes a deployment pipeline on AWS. Or deploy the pipeline manually with this button: 

<a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=cfn-stack-notifications-deployment-pipeline&templateURL=https://s3.amazonaws.com/jeshan-oss-public-files/cfn-stack-notifications-deployment-pipeline-template.yaml">
<img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"/>
</a>

## Infrastructure
This is what will get deployed:

![](/diagram.png)

![](/diagram-base.png)


# Adding private sceptre configuration
The build process also generates boilerplate configuration with `python generate-config.py`.

You have the ability to provide sceptre with the necessary configuration and credentials that you will want to keep private.
Read the buildspec for this, in particular:
`aws s3 sync s3://${PRIVATE_BUCKET}/github.com/$REPO/master .`

To generate sceptre configuration for a private environment, you can run something like:
`python generate-config.py production`



You can place your private sceptre configuration at that location in a private bucket and they will be pulled on build.
There's a script available to send these files to S3: Edit your private bucket in `upload-private-config.sh` and run it.
You need to create the role so that your deployment pipeline has permissions to deploy. run `python put-target-deployment-roles.py`
Add the target account number in `config/app/${ENV}/config.yaml`.
Then, run the pipeline. That's all what's needed for sceptre to work.
