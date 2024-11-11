# Schema RAG 

We are building a RAG system for data schema 
- We will be first reading all the schema files available in schema registry 
- We will try to determine the basic canonical types for the columns from the schema files and remove redundent columns from the schema for reuse 
- After the canonical type is determined we will read sample data form data-store to determine the data-dictionary of the columns 
- We will map data-dictionary, description and data-type of the column from the sample data and schema definition (data source is in GCP BigQuery data-store)
- There is a mapping of data-dictionary to data-classification will determine the data-classification and place it in canonical type file 


- From here given a schema we need to find the canonical type of the columns if the canonical type is not found create a new one if exist already repond with the existing canonical type and other details.

- We are going to ignore timestamp fields for this exercise 


## Code Structure 

src/components/
- schema_registry.py
- data_dictionary.py
- canonical_types.py

src/config/
- config.yaml

src/utils/
- logger.py


src/tests/
- test_schema_registry.py
- test_data_dictionary.py
- test_canonical_types.py

