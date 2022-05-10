## Lab: Serverless Functions
## Overview
**Deploy a serverless function to the cloud**.

**Feature Tasks and Requirements**:

1. [x] Sign up with [Vercel](https://vercel.com/docs/get-started)
2. [x] Create a repository on Github and link it to Vercel account.
3. [x] Use [requests](https://docs.python-requests.org/en/latest/) library to interact with REST [Countries API](https://restcountries.com/#rest-countries)
4. [x] Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:
5. [x] The serverless function should handle a GET http request with a given country name that responds with a string with the form The capital of X is Y
6. [x] E.g./capital-finder?country=Chile should generate an http response of The capital of Chile is Santiago.
7. [x] The serverless function should handle a GET http request with a given capital that responds with a string with the form The capital of X is Y
8. [x] E.g./capital-finder?capital=Santiago should generate an http response of Santiago is the capital of Chile.

## Deployed Functions
[Capital](https://capital-finder-thomas-basham.vercel.app/api/countries?capital=Santiago)

[Country](https://capital-finder-thomas-basham.vercel.app/api/countries?country=chile)

## Resources
[Vercel](https://vercel.com/docs/concepts/functions/serverless-functions/supported-languages#python)

[Vercel Cli](https://vercel.com/docs/concepts/deployments/overview#vercel-cli)
