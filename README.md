# cfn-stack-notifications

Sets up an SNS topic for all your stacks in all regions.

This will be useful when you want to track deployments. The SNS topics can relay messages to many destinations, including AWS Lambda. This means you can subscribe a function to the topic and send deployment events to your chatbot. 


If you use [sceptre](https://github.com/cloudreach/sceptre), you can deploy this in all regions in one step with:

`sceptre launch -y dev`


Note that this project is still experimental. Please share your experiences with the community.
