# cfn-stack-notifications

Sets up an SNS topic for all your stacks in all regions.

This will be useful when you want to track deployments. The SNS topics can relay messages to many destinations, including AWS Lambda. This means you can subscribe a function to the topic and send deployment events to your chatbot. 


If you use [sceptre](https://github.com/cloudreach/sceptre), you can deploy this in all regions in one step with:

`sceptre launch -y dev`

or deploy per region with this button: 

<a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=cfn-stack-notifications&templateURL=https://s3.amazonaws.com/jeshan-oss-public-files/cfn-stack-notifications-template.yaml">
<img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"/>
</a>


Note that this project is still experimental. Please share your experiences with the community.

Also, note that it relies on CloudTrail already set up. You can set one with the following snippet:

```yaml
Trail:
  Type: AWS::CloudTrail::Trail
  DependsOn: TrailBucketPolicy
  Properties:
    IncludeGlobalServiceEvents: true
    IsLogging: true
    IsMultiRegionTrail: true
    S3BucketName: !Ref TrailBucket

TrailBucket:
  Type: AWS::S3::Bucket

TrailBucketPolicy:
  Type: AWS::S3::BucketPolicy
  Properties:
    Bucket: !Ref TrailBucket
    PolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Action: s3:GetBucketAcl
          Effect: Allow
          Principal:
            Service: cloudtrail.amazonaws.com
          Resource: !Sub '${TrailBucket.Arn}'
        - Action: s3:PutObject
          Condition:
            StringEquals:
              s3:x-amz-acl: bucket-owner-full-control
          Effect: Allow
          Principal:
            Service: cloudtrail.amazonaws.com
          Resource: !Sub ${TrailBucket.Arn}/AWSLogs/${AWS::AccountId}/*
```
