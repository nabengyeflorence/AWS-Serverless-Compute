# AWS-Serverless-Compute
Contact Form with AWS API Gateway, Lambda, and SES

This project demonstrates how to create a contact form that sends an
email using AWS services: API Gateway, Lambda, and Amazon SES.

# Architecture Overview

1.  Contact Form (Frontend)
    Users fill in a contact form on a website and submit their details.

2.  Amazon API Gateway
    Exposes a REST API endpoint that the contact form submits data to
    (via HTTP POST).

3.  AWS Lambda
    Processes the submitted data and uses Amazon SES to send an email.

4.  Amazon SES (Simple Email Service)
    Sends the email to the recipient. In sandbox mode, only verified
    sender and recipient email addresses can be used.


# Setup Instructions

1. Verify Emails in SES

-   Go to the SES Console.
-   Navigate to Verified Identities.
-   Verify both the sender and recipient email addresses (mandatory in
    sandbox mode).

2. Create the Lambda Function

3. Create API Gateway

-   Create a REST API in API Gateway.
-   Create a POST method for the resource path (e.g., /contact).
-   Integrate it with your Lambda function.
-   Deploy the API and note the Invoke URL.

4. Update the Frontend Form

-   Your contact form should submit data to the API Gateway endpoint
    (POST).

# Notes

-   SES Sandbox Mode: You must verify both the sender and recipient
    emails.
-   To send to unverified emails, request SES production access in the
    AWS console.
-   Ensure the SES region matches the Lambda region.




