# Financial Studies
Repository to study data access and machine learning using financial data

## Data structure

I'll be given three datasets, containing:
* A: person information and list of debts
* B: person rating, list of assets and source of income
* C: last person searches from bureaus, cash flow and credit card purchases information

## Data disponibility and criticity

Data must be easy and fast to access for the dataset C, but doesn't need to be fast for the dataset A.
Data must be considered critical and secure for the dataset A, but doesn't for the dataset C.
So:
* Dataset A: critical security, but not full performance required
* Dataset B: middle term
* Dataset C: no critical data, but need to be easily (fast) accesible

## Solution infraestructure

My first tought is to use the AWS structure to hold, process and access data from the different datasets.
AWS has a lot of resources and can monitor and scale the servers as needed.
The main solutions would be:
* AWS Api Gateway can be used to create endpoints and retrieve data as JSON
* AWS Cognito for authentication
  * maybe basic authentication for dataset C, but some more complex token and crypto based security for dataset A
* AWS DynamoDB for data persistance
  * NoSQL databases can be faster then relational databases, so it can be a very efficient solution for the dataset C.
  * But it will be the best solution for the first two datasets?
* AWS Lambda to communicate DynamoDB with API Gateway
  * It may be used to process machine learning algoritms with some work (compiling libraries to the aws environment, like lambda and scikit leaning)
  * There are solutions already available?

## Specific solutions
* [Databases](/database.md)
* [Api Gateway](api-gateway.md)
* [Lambda Functions](lambda.md)