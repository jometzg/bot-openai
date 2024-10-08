# this one needs some work. May be better to convert to JSON
# to be able to add the new user request after all of the other messages

import os
from azure.cosmos import CosmosClient, PartitionKey, exceptions

# Initialize the Cosmos client
endpoint = os.getenv("COSMOS_DB_ENDPOINT")
key = os.getenv("COSMOS_DB_KEY")
database_name = os.getenv("COSMOS_DB_DATABASE", "responsecache")
container_name = os.getenv("COSMOS_DB_CONTAINER", "responses")

# client = CosmosClient(endpoint, key)
# database = client.get_database_client(database_name)
# container = database.get_container_client(container_name)

def write_document(document: dict, partition_key: str) -> None:
    """
    Writes a document to the Cosmos DB container.

    Args:
        document (dict): The document to write to Cosmos DB.
        partition_key (str): The partition key for the document.
    """
    try:
        client = CosmosClient(endpoint, key)
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)
        document['partitionKey'] = partition_key
        document['id'] = partition_key
        container.replace_item(document['id'], document)
        #container.create_item(body=document)
        print("Document written to Cosmos DB successfully.")
    except exceptions.CosmosHttpResponseError as e:
        print(f"An error occurred: {e.message}")

def read_document(document_id: str) -> dict:
    """
    Reads a document from the Cosmos DB container.

    Args:
        document_id (str): The ID of the document to read.
        partition_key (str): The partition key of the document.

    Returns:
        dict: The document read from Cosmos DB.
    """
    try:
        client = CosmosClient(endpoint, key)
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)
        response = container.read_item(item=document_id, partition_key=document_id)
        print("Document read from Cosmos DB successfully.")
        return response
    except exceptions.CosmosHttpResponseError as e:
        print(f"An error occurred: {e.message}")
        return None

# Example usage
if __name__ == "__main__":
    # Example document

    document = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "what is a meme"}
            ],
            "max_tokens": 150,
            "temperature": 0.7
            }

    # Write the document to Cosmos DB
    write_document(document, "exampleId")

    # Read the document from Cosmos DB
    returneddoc = read_document("exampleId")
    print(returneddoc)
    # add a new message section with role user and content "what is a meme"
    new_message = {"role": "assistant", "content": "an idea"}  
    document["messages"].append(new_message) 
    write_document(document, "exampleId")
