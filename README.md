# Serverless Approval System

## Overview

A serverless approval system that automates request submissions and manager approvals. This microservice enables team members to submit requests, which trigger automated notifications to managers. Managers can then approve or deny requests, with status updates tracked in real-time through a dynamic status queue.

## How It Works

1. **Submit Request** - A team member submits a request through the API
2. **Trigger Approval** - Lambda function processes the request and sends it to the manager for approval
3. **Manager Decision** - Manager approves or denies the request
4. **Status Updates** - The request status is updated and tracked throughout the workflow

## Technology Stack

- **AWS Lambda** - Serverless compute for request processing and notifications
- **AWS Step Functions** - Orchestrates the approval workflow
- **API Gateway** - Exposes endpoints for request submissions and status checks
- **DynamoDB** - NoSQL database for storing requests and status information
- **IAM Roles** - Manages secure access and permissions between services

## Security & Monitoring

This system provides enterprise-grade security and compliance features:

- **AWS CloudTrail** - Tracks and logs all API calls and activities for complete audit trails
- **Comprehensive Metrics** - Monitors system performance and user actions for analytics and decision-making
- **Access Control** - IAM roles enforce least-privilege access across all services
- **Audit Ready** - All request submissions, approvals, and denials are logged for compliance and security reviews

This creates a secure foundation for organizations that need to monitor and audit employee/user requests while ensuring data integrity and accountability throughout the approval workflow.

## Use Case

This template is ideal for teams building automated workflows within their AWS environment, such as:
- Leave request approvals
- Budget or expense approvals
- Certificate or credential requests
- Any workflow requiring manager review and decision

*Note:
- This template serves as a guide. That said, the notify_manager.py lambda function prints a taskToken to CloudWatch so it can be copied manually. In real life, a SNS or SES would be invoked to automate notifications.