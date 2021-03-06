# dynamodb_event_reader

Sample SAM Template for dynamodb_event_reader to interact with DynamoDB Events.

## Requirements

* AWS CLI already configured with at least PowerUser permission

* [Python 3 installed](https://www.python.org/downloads/)

* [Docker installed](https://www.docker.com/community-edition)
* [SAM Local installed](https://github.com/awslabs/aws-sam-local)

### Build Your Application

When you make a change to the code, you can run the following command to install dependencies and convert your Lambda
function source code into an artifact that can be deployed and run on Lambda.

```bash
sam build
```

### Local development

Assuming you have already built your application, run the following to invoke your function locally:

**Invoking function locally without API Gateway**

```bash
sam local generate-event dynamodb update | sam local invoke ReadDynamoDBEvent
```

You can also specify a `event.json` file with the payload you'd like to invoke your function with:

```bash
sam local invoke -e event.json ReadDynamoDBEvent
```

## Deployment

First and foremost, we need a S3 bucket where we can upload our Lambda functions packaged as ZIP before we deploy
anything - If you don't have a S3 bucket to store code artifacts then this is a good time to create one:

```bash
aws s3 mb s3://BUCKET_NAME
```

Now build your Lambda function

```bash
sam build
```

Provided you have a S3 bucket created, run the following command to package our Lambda function to S3:

```bash
sam package \
    --output-template-file packaged.yaml \
    --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME
```

Next, the following command will create a Cloudformation Stack and deploy your SAM resources.

```bash
sam deploy \
    --template-file packaged.yaml \
    --stack-name dynamodb_event_reader \
    --capabilities CAPABILITY_IAM
```

> **See [Serverless Application Model (SAM) HOWTO Guide](https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md) for more details in how to get started.**

# Appendix

## AWS CLI commands

AWS CLI commands to package, deploy and describe outputs defined within the cloudformation stack:

```bash
sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME

sam deploy \
    --template-file packaged.yaml \
    --stack-name dynamodb_event_reader \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides MyParameterSample=MySampleValue

aws cloudformation describe-stacks \
    --stack-name dynamodb_event_reader --query 'Stacks[].Outputs'
```
