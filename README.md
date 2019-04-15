# cfn-stack-notifications

Sets up an SNS topic for all your stacks in all regions.

This will be useful when you want to track deployments. The SNS topics can relay messages to many destinations, including AWS Lambda. This means you can subscribe a function to the topic and send deployment events to your chatbot. 


If you use [sceptre](https://github.com/cloudreach/sceptre), you can deploy this in all regions in one step with:

`sceptre launch -y dev`

or deploy with this button: 

<a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=myteststack&templateURL=https://s3.amazonaws.com/jeshan-oss-public-files/cfn-stack-notifications-template.yaml">
<img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"/>
</a>


Note that this project is still experimental. Please share your experiences with the community.
