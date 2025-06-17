from flask import Flask, render_template, request
from supabase import create_client
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

ITEMS_PER_PAGE = int(os.getenv("ITEMS_PER_PAGE")  # Number of items to show per page

@app.route('/')
def index():
    # Get filter parameters from request
    symbol = request.args.get('symbol', '')
    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    page = int(request.args.get('page', 1))
    
    # Start building the query
    query = supabase.table('stock_current').select('*')
    
    # Apply date range filters if they exist
    try:
        if start_date:
            start_dt = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
            query = query.gte('timestamp', start_dt.isoformat())
        
        if end_date:
            end_dt = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
            query = query.lte('timestamp', end_dt.isoformat())
    except ValueError:
        pass  # If dates are invalid, ignore them
    
    # Execute the query
    response = query.execute()
    
    # Get the data and columns
    data = response.data
    if data:
        # Exclude 'id' from columns
        columns = [col for col in data[0].keys() if col != 'id']
    else:
        columns = []
        data = []
    
    # Filter the results in Python for partial matching
    if symbol and data:
        symbol_upper = symbol.upper()
        filtered_data = []
        for row in data:
            # Convert both strings to uppercase and check if the search term is in the symbol
            if symbol_upper in str(row['symbol']).upper():
                filtered_data.append(row)
        data = filtered_data
    
    # Calculate pagination
    total_items = len(data)
    total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
    start_idx = (page - 1) * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    
    # Get the current page's data
    paginated_data = data[start_idx:end_idx]
    
    return render_template('index.html', 
                         columns=columns, 
                         data=paginated_data,
                         current_page=page,
                         total_pages=total_pages,
                         total_items=total_items)

if __name__ == '__main__':
    app.run(debug=True)