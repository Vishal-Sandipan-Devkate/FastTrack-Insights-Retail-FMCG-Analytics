import streamlit as st
import plotly.express as px
import pandas as pd

# Function to display options based on selected operation
def display_options(operation):
    if operation == 'Market Basket Analysis':
        st.subheader('Select Operation')
        options = [
            'Number of Sales Weekly',
            'Number of Customers Weekly',
            'Sales per Customer Weekly',
            'Frequency of the Items Sold',
            'Top Customers regarding Number of Items bought',
            'Number of Sales per Discrete Week Days',
            'Number of Sales per Discrete Months',
            'Number of Sales per Discrete Month Days',  
            'Recency Distribution of the Customers',
            'Visit Frequency Distribution of the Customers',
            'Monetary Distribution of the Customers',
            'RFM Scores/RFM Segments',
            'Relationship between Visit_Frequency and Recency'
        ]
        selected_operation = st.selectbox('Select Operation', options)
        st.write('You selected:', selected_operation)

        # Load dataset
        data = pd.read_csv('D:/projecttt/Retail Operation/Groceries_dataset.csv')
        data.columns = ['memberID', 'Date', 'itemName']
        data.memberID = data['memberID'].astype('str')
        data['Date'] = pd.to_datetime(data['Date'])


        # Lets Start with the calculate the Recency

        # Finding last purchase date of each customer
        Recency = data.groupby(by='memberID')['Date'].max().reset_index()
        Recency.columns = ['memberID', 'LastDate']
        Recency.head()

                # Finding last date for our dataset
        last_date_dataset = Recency['LastDate'].max()
        last_date_dataset

        # Lets Start with the calculate the Recency

        # Finding last purchase date of each customer

        # If the selected operation is 'Number of Sales Weekly'
        if selected_operation == 'Number of Sales Weekly':
            # Calculate number of sales weekly
            sales_weekly = data.resample('W', on='Date').size().reset_index(name='Number of Sales')

            # Plot the graph
            fig = px.line(sales_weekly, x='Date', y='Number of Sales', labels={'Number of Sales': 'Number of Sales Weekly'})
            st.plotly_chart(fig)

        # If the selected operation is 'Number of Customers Weekly'    
        elif selected_operation == 'Number of Customers Weekly':
    # Calculate number of unique customers weekly
            unique_customers_weekly = data.resample('W', on='Date')['memberID'].nunique().to_frame(name='Number of Customers')
    # Plot the graph
            fig = px.line(unique_customers_weekly, x=unique_customers_weekly.index, y='Number of Customers', labels={'Number of Customers': 'Number of Customers Weekly'})
            st.plotly_chart(fig)


        elif selected_operation == 'Sales per Customer Weekly':
    # Calculate number of sales weekly
            sales_weekly = data.resample('W', on='Date').size()

        # Calculate number of unique customers weekly
            unique_customers_weekly = data.resample('W', on='Date')['memberID'].nunique()

        # Calculate Sales per Customer Weekly
            sales_per_customer_weekly = sales_weekly / unique_customers_weekly

        # Plot the graph
            fig = px.line(sales_per_customer_weekly, x=sales_per_customer_weekly.index, y=sales_per_customer_weekly,
                    labels={'y': 'Sales per Customer Ratio'})
            fig.update_layout(title_text='Sales per Customer Weekly',
                        title_x=0.5, title_font=dict(size=18))
            fig.update_yaxes(rangemode="tozero")
            st.plotly_chart(fig)

        elif selected_operation == 'Frequency of the Items Sold':
    # Calculate frequency of items sold
            frequency_of_items = data.groupby('itemName').size().reset_index(name='count')

            # Plot the graph
            fig = px.treemap(frequency_of_items, path=['itemName'], values='count')
            fig.update_layout(title_text='Frequency of the Items Sold', title_x=0.5, title_font=dict(size=18))
            fig.update_traces(textinfo="label+value")
            st.plotly_chart(fig)

        elif selected_operation == 'Top Customers regarding Number of Items bought':
            # Calculate number of items bought by each customer
            user_item = data.groupby('memberID').size().reset_index(name='count').sort_values(by='count', ascending=False)
            
            # Plot the graph
            fig = px.bar(user_item.head(20), x='memberID', y='count',
                        labels={'y': 'Number of Items Bought', 'count': 'Number of Sales'},
                        color='count')
            fig.update_layout(title_text='Top 20 Customers regarding Number of Items Bought',
                            title_x=0.5, title_font=dict(size=18))
            fig.update_traces(marker=dict(line=dict(color='#E0FF43', width=1)))
            st.plotly_chart(fig)

        elif selected_operation == 'Number of Sales per Discrete Week Days':
            # Calculate number of sales per discrete week days
            day = data.groupby(data['Date'].dt.strftime('%A'))['itemName'].count()
            
            # Plot the graph
            fig = px.bar(day, x=day.index, y=day, color=day,
                        labels={'y': 'Number of Sales', 'Date': 'Week Days'})
            fig.update_layout(title_text='Number of Sales per Discrete Week Days',
                            title_x=0.5, title_font=dict(size=18))
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            st.plotly_chart(fig)

        elif selected_operation == 'Number of Sales per Discrete Months':
            # Calculate number of sales per discrete months
            month = data.groupby(data['Date'].dt.strftime('%m'))['itemName'].count()
            
            # Plot the graph
            fig = px.bar(month, x=month.index, y=month, color=month,
                        labels={'y': 'Number of Sales', 'Date': 'Months'})
            fig.update_layout(title_text='Number of Sales per Discrete Months',
                            title_x=0.5, title_font=dict(size=18))
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            st.plotly_chart(fig)

        elif selected_operation == 'Number of Sales per Discrete Month Days':
    # Calculate number of sales per discrete month days
            month_day = data.groupby(data['Date'].dt.strftime('%d'))['itemName'].count()
            
            # Plot the graph
            fig = px.bar(month_day, x=month_day.index, y=month_day, color=month_day,
                        labels={'y': 'Number of Sales', 'Date': 'Month Days'})
            fig.update_layout(title_text='Number of Sales per Discrete Month Days',
                            title_x=0.5, title_font=dict(size=18))
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            st.plotly_chart(fig)


        elif selected_operation == 'Recency Distribution of the Customers':
    # Assuming you have a DataFrame named Recency containing the recency values
    # You need to replace Recency with your actual DataFrame name
            Recency = data.groupby(by='memberID')['Date'].max().reset_index()
            Recency.columns = ['memberID', 'LastDate']
            Recency.head()

            # Finding last date for our dataset
            last_date_dataset = Recency['LastDate'].max()
            last_date_dataset

            # Calculating Recency by subtracting (last transaction date of dataset) and (last purchase date of each customer)
            Recency['Recency'] = Recency['LastDate'].apply(lambda x: (last_date_dataset - x).days)
            Recency.head()
    
            # Plot the histogram
            fig = px.histogram(Recency, x='Recency', opacity=0.85, marginal='box')
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            fig.update_layout(title_text='Recency Distribution of the Customers', title_x=0.5, title_font=dict(size=20))
            st.plotly_chart(fig)


        elif selected_operation == 'Visit Frequency Distribution of the Customers':
            # Assuming you have a DataFrame named Frequency containing the visit frequency values
            # You need to replace Frequency with your actual DataFrame name
            # Frequency of the customer visits
            Frequency = data.drop_duplicates(['Date', 'memberID']).groupby(by=['memberID'])['Date'].count().reset_index()
            Frequency.columns = ['memberID', 'Visit_Frequency']
            Frequency.head()
        
            # Plot the histogram
            fig = px.histogram(Frequency, x='Visit_Frequency', opacity=0.85, marginal='box')
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            fig.update_layout(title_text='Visit Frequency Distribution of the Customers', title_x=0.5, title_font=dict(size=20))
            st.plotly_chart(fig)


        elif selected_operation == 'Monetary Distribution of the Customers':
            # Assuming you have a DataFrame named Monetary containing the monetary values
            # You need to replace Monetary with your actual DataFrame name
            Monetary = data.groupby(by="memberID")['itemName'].count().reset_index()
            Monetary.columns = ['memberID', 'Monetary']
            Monetary.head()

                        # I assumed each item has equal price and price is 10
            Monetary['Monetary'] = Monetary['Monetary'] * 10
            Monetary.head()
                        
            # Plot the histogram
            fig = px.histogram(Monetary, x='Monetary', opacity=0.85, marginal='box',
                            labels={'Monetary': 'Monetary'})
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            fig.update_layout(title_text='Monetary Distribution of the Customers', title_x=0.5, title_font=dict(size=20))
            st.plotly_chart(fig)

        elif selected_operation == 'RFM Scores/RFM Segments':
            # Calculate Recency
            Recency = data.groupby(by='memberID')['Date'].max().reset_index()
            Recency.columns = ['memberID', 'Recency']
            
            # Calculate Frequency
            # You need to calculate Frequency based on your dataset
            # Frequency of the customer visits
            Frequency = data.drop_duplicates(['Date', 'memberID']).groupby(by=['memberID'])['Date'].count().reset_index()
            Frequency.columns = ['memberID', 'Visit_Frequency']
    
            # Calculate Monetary
            # You need to calculate Monetary based on your dataset.

            Monetary = data.groupby(by="memberID")['itemName'].count().reset_index()
            Monetary.columns = ['memberID', 'Monetary']
            Monetary['Monetary'] = Monetary['Monetary'] * 10
            
            
            
            # Combine all scores into one DataFrame
            RFM = pd.concat([Recency['memberID'], Recency['Recency'], Frequency['Visit_Frequency'], Monetary['Monetary']], axis=1)
            
            # Calculate RFM Quartiles and RFM Score
            # You need to calculate RFM quartiles and score based on your business logic

            # 5-5 score = the best customers
            RFM['Recency_quartile'] = pd.qcut(RFM['Recency'], 5, [5, 4, 3, 2, 1])
            RFM['Frequency_quartile'] = pd.qcut(RFM['Visit_Frequency'], 5, [1, 2, 3, 4, 5])

            RFM['RF_Score'] = RFM['Recency_quartile'].astype(str) + RFM['Frequency_quartile'].astype(str)
            RFM.head()
            
            # Map RFM Score to RFM Segment
            # You need to define your RFM segments mapping logic
                        
            segt_map = {  # Segmentation Map [Ref]
                r'[1-2][1-2]': 'hibernating',
                r'[1-2][3-4]': 'at risk',
                r'[1-2]5': 'can\'t loose',
                r'3[1-2]': 'about to sleep',
                r'33': 'need attention',
                r'[3-4][4-5]': 'loyal customers',
                r'41': 'promising',
                r'51': 'new customers',
                r'[4-5][2-3]': 'potential loyalists',
                r'5[4-5]': 'champions'
            }

            RFM['RF_Segment'] = RFM['RF_Score'].replace(segt_map, regex=True)
            RFM.head()
            
            # Count the occurrences of each RFM segment
            x = RFM['RF_Segment'].value_counts()
            
            # Plot the treemap
            fig = px.treemap(x, path=[x.index], values=x)
            fig.update_layout(title_text='Distribution of the RFM Segments', title_x=0.5, title_font=dict(size=20))
            fig.update_traces(textinfo="label+value+percent root")
            st.plotly_chart(fig)
            

        elif selected_operation == 'Relationship between Visit_Frequency and Recency':
            # Plot the scatter plot
            # Combining all scores into one DataFrame
            # Finding the last purchase date of each customer
            Recency = data.groupby(by='memberID')['Date'].max().reset_index()
            Recency.columns = ['memberID', 'Recency']

            # Frequency of the customer visits
            Frequency = data.drop_duplicates(['Date', 'memberID']).groupby(by=['memberID'])['Date'].count().reset_index()
            Frequency.columns = ['memberID', 'Visit_Frequency']
            # Frequency.head()

            Monetary = data.groupby(by="memberID")['itemName'].count().reset_index()
            Monetary.columns = ['memberID', 'Monetary']
            # Monetary.head()

            # I assumed each item has equal price and price is 10
            Monetary['Monetary'] = Monetary['Monetary'] * 10
            Monetary.head()

            RFM = pd.concat([Recency['memberID'], Recency['Recency'], Frequency['Visit_Frequency'], Monetary['Monetary']], axis=1)
            # RFM.head()

            # 5-5 score = the best customers
            RFM['Recency_quartile'] = pd.qcut(RFM['Recency'], 5, [5, 4, 3, 2, 1])
            RFM['Frequency_quartile'] = pd.qcut(RFM['Visit_Frequency'], 5, [1, 2, 3, 4, 5])

            RFM['RF_Score'] = RFM['Recency_quartile'].astype(str) + RFM['Frequency_quartile'].astype(str)
            # RFM.head()

            
            segt_map = {  # Segmentation Map [Ref]
                r'[1-2][1-2]': 'hibernating',
                r'[1-2][3-4]': 'at risk',
                r'[1-2]5': 'can\'t loose',
                r'3[1-2]': 'about to sleep',
                r'33': 'need attention',
                r'[3-4][4-5]': 'loyal customers',
                r'41': 'promising',
                r'51': 'new customers',
                r'[4-5][2-3]': 'potential loyalists',
                r'5[4-5]': 'champions'
            }

            RFM['RF_Segment'] = RFM['RF_Score'].replace(segt_map, regex=True)
            # RFM.head()
            fig = px.scatter(RFM, x="Visit_Frequency", y="Recency", color='RF_Segment',
                            labels={"Visit_Frequency": "Visit Frequency", "Recency": "Recency"})
            fig.update_layout(title_text='Relationship between Visit Frequency and Recency', title_x=0.5, title_font=dict(size=20))
            st.plotly_chart(fig)





    elif operation == 'Price Prediction':
        # Add code for price prediction operation
        pass
    elif operation == 'Others':
        # Add code for other operations
        pass

# Main function to run the Streamlit app
def main():
    st.title('Grocery Store Analysis')
    st.sidebar.header('Options')
    operation = st.sidebar.selectbox('Operation', ['Market Basket Analysis', 'Price Prediction', 'Others'])
    display_options(operation)

if __name__ == '__main__':
    main()
