## Lab: Serverless Functions
## Overview
Deploy a serverless function to the cloud.
Feature Tasks and Requirements

1. [x] Sign up with Vercel.
2. [x] Create a repository on Github and link it to Vercel account.
3. [ ] Use requests library to interact with REST Countries API
4. [ ] Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:
5. [ ] The serverless function should handle a GET http request with a given country name that responds with a string with the form The capital of X is Y
6. [ ] E.g./capital-finder?country=Chile should generate an http response of The capital of Chile is Santiago.
7. [ ] The serverless function should handle a GET http request with a given capital that responds with a string with the form The capital of X is Y
8. [ ] E.g./capital-finder?capital=Santiago should generate an http response of Santiago is the capital of Chile.
