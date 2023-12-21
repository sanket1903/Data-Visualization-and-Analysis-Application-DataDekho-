# Load important libraries
import pandas as pd
import streamlit as st
import os

def app():
    """This application is created to help the user change the metadata for the uploaded file.
    They can perform merges, change column names, and so on.
    """

    # Load the uploaded data
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        data = pd.read_csv('data/main_data.csv')
        st.dataframe(data)

        # Read the column metadata for this dataset
        col_metadata = pd.read_csv('data/metadata/column_type_desc.csv')

        ''' Change the information about column types
            Here the info of the column types can be changed using dropdowns.
            The page is divided into two columns using Beta columns 
        '''
        st.markdown("#### Change the information about column types")

        # Use two column technique
        col1, col2 = st.columns(2)

        # Design column 1
        name = col1.selectbox("Select Column", data.columns)

        # Design column two
        current_metadata = col_metadata[col_metadata['column_name'] == name]
        current_type = current_metadata['type'].values[0] if not current_metadata.empty else None
        column_options = ['numeric', 'categorical', 'object']
        current_index = column_options.index(current_type) if current_type in column_options else 0

        with col2.form("metadata_form"):
            type = st.selectbox("Select Column Type", options=column_options, index=current_index)
            submit_button = st.form_submit_button("Change Column Type")

        st.write("""Select your column name and the new type from the data.
                    To submit all the changes, click on *Submit changes* """)

        if submit_button:
            # Set the value in the metadata and resave the file
            st.dataframe(current_metadata)

            col_metadata.loc[col_metadata['column_name'] == name, 'type'] = type
            col_metadata.to_csv('data/metadata/column_type_desc.csv', index=False)

            st.write("Your changes have been made!")
            st.dataframe(col_metadata[col_metadata['column_name'] == name])


