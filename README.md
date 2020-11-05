# OrderTracker

Order tracker that uses pdfs generated from Wix Restaurants to create a ticket system to read and interact with

## Features

- Parser that parses standardized PDFs from Wix Restaurants to pull out a list of items ordered
  - Outputs a JSON object that has
    - a list of items with each items customizations
    - Customer Name
    - Total
    - Delivery Date

- Angular Front end to display each order
  - open order to display order in more detail
  - click items to cross them off the list

## Technologies
- Angular
- Python
