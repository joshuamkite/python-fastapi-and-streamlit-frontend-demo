import os
import requests
import streamlit as st
import pandas as pd


api_url = os.getenv('API_URL', 'http://localhost:8000')


def list_all_products():
    """  returns json map of  all products"""
    url = f'{api_url}/products'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        error_detail = response.json().get('detail', 'Unknown error')
        return f"Error {response.status_code}: {error_detail}"


def display_products(api_response):
    """Display products in a table"""
    # Convert to pandas DataFrame
    df = pd.DataFrame(api_response)
    # Format price as currency
    df['price'] = df['price'].apply(lambda x: f"{x:.2f}")
    # Display as interactive dataframe
    st.dataframe(df, use_container_width=True)


def get_product_by_id(product_id):
    """match and return on product_id"""
    url = f'{api_url}/products/{product_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        error_detail = response.json().get('detail', 'Unknown error')
        return f"Error {response.status_code}: {error_detail}"


def add_product(id, name, price, stock_quantity):
    """Add a new product"""
    url = f'{api_url}/products'
    response = requests.post(url, json={
        "id": id,
        "name": name,
        "price": price,
        "stock_quantity": stock_quantity
    })
    if response.status_code == 200:
        return response.json()
    else:
        error_detail = response.json().get('detail', 'Unknown error')
        return f"Error {response.status_code}: {error_detail}"


def update_product(id, name, price, stock_quantity):
    """Update a product"""
    url = f'{api_url}/products/{id}'
    response = requests.put(url, json={
        "id": id,
        "name": name,
        "price": price,
        "stock_quantity": stock_quantity
    })
    if response.status_code == 200:
        return response.json()
    else:
        error_detail = response.json().get('detail', 'Unknown error')
        return f"Error {response.status_code}: {error_detail}"


def delete_product(id):
    """Delete a product"""
    url = f'{api_url}/products/{id}'
    response = requests.delete(url, json={
        "id": id
    })
    if response.status_code == 200:
        return response.json()
    else:
        error_detail = response.json().get('detail', 'Unknown error')
        return f"Error {response.status_code}: {error_detail}"


st.title('API Caller Demo')
st.write('Call locally hosted API using Streamlit')

# List all products

if st.button('List all products'):
    api_response = list_all_products()
    display_products(api_response)


# Get a product by ID

get_product_by_id_label = "get a product from its ID"
st.expander(get_product_by_id_label, expanded=False, icon=None)
with st.expander(get_product_by_id_label, expanded=False):

    id = st.text_input('Get details for a product by its ID (Overwrite to change)', '1')

    if st.button('get a product from its ID'):
        api_response = get_product_by_id(id)
        display_products([api_response])

# Add a product

add_label = "add a product"
st.expander(add_label, expanded=False, icon=None)
with st.expander("add a product", expanded=False):

    id_new = st.text_input('New product ID (Overwrite to change)', '4')
    name_new = st.text_input('New product name (Overwrite to change)', 'Dragon Fruit')
    price_new = st.text_input('New product item price (Overwrite to change)', '1.00')
    stock_quantity_new = st.text_input('New product quantity (Overwrite to change)', '10')

    if st.button('Add a new product'):
        api_response = add_product(
            int(id_new),
            name_new,
            float(price_new),
            int(stock_quantity_new)
        )
        if isinstance(api_response, dict):  # Only display table if response is a product object
            display_products([api_response])
        else:
            st.write(api_response)

# Update a product

update_label = "update a product"
st.expander(update_label, expanded=False, icon=None)
with st.expander("update a product", expanded=False):

    id_updating = st.text_input('Product ID to update (Overwrite to change)', '1')
    name_updating = st.text_input('Product name to update (Overwrite to change)', 'apple')
    price_updating = st.text_input('Product item price to update (Overwrite to change)', '0.40')
    stock_updating = st.text_input('Product quantity to update (Overwrite to change)', '50')

    if st.button('Update a product'):
        update_response = update_product(
            int(id_updating),
            name_updating,
            float(price_updating),
            int(stock_updating)
        )
        if isinstance(update_response, dict):  # Only display table if response is a product object
            display_products([update_response])
        else:
            st.write(update_response)

# Delete a product

delete_label = "delete a product"
st.expander(delete_label, expanded=False, icon=None)

with st.expander("delete a product", expanded=False):

    id_deleting = st.text_input('Product ID to delete (Overwrite to change)', '1')

    if st.button('Delete a product'):
        update_response = delete_product(
            int(id_deleting)
        )
        if isinstance(update_response, dict):  # Only display table if response is a product object
            display_products([update_response])
        else:
            st.write(update_response)
