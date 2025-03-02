# ===========================================================================
# FOR DEMO ONLY.
# For pentesting - https://www.hacksplaining.com/lessons/sql-injection
# ==========================================================================
from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3
import urllib.parse

# Set up the database
def setup_database():
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    
    # Drop tables if they exist
    cursor.execute("DROP TABLE IF EXISTS Products")
    cursor.execute("DROP TABLE IF EXISTS Users")
    
    # Create Products table
    cursor.execute('''
    CREATE TABLE Products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        price REAL
    )
    ''')
    
    # Create Users table (this is the "sensitive" data)
    cursor.execute('''
    CREATE TABLE Users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        email TEXT,
        role TEXT
    )
    ''')
    
    # Insert sample products
    products = [
        (1, 'Laptop', 'High-performance laptop', 999.99),
        (2, 'Smartphone', 'Latest model smartphone', 699.99),
        (3, 'Tablet', '10-inch screen tablet', 349.99),
        (4, 'Headphones', 'Noise-cancelling headphones', 149.99),
        (5, 'Smartwatch', 'Fitness tracking smartwatch', 199.99)
    ]
    cursor.executemany('INSERT INTO Products VALUES (?,?,?,?)', products)
    
    # Insert sample users (in a real system, passwords would be hashed)
    users = [
        (1, 'admin', 'admin123', 'admin@example.com', 'administrator'),
        (2, 'john', 'password123', 'john@example.com', 'user'),
        (3, 'sarah', 'securepass', 'sarah@example.com', 'user'),
        (4, 'mike', 'mike1234', 'mike@example.com', 'moderator'),
        (5, 'jessica', 'jessica123', 'jessica@example.com', 'user')
    ]
    cursor.executemany('INSERT INTO Users VALUES (?,?,?,?,?)', users)
    
    conn.commit()
    conn.close()
    print("Database initialized with sample data")

class VulnerableHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Parse the URL
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)
        
        # Vulnerable page that performs a SQL query based on user input
        if parsed_path.path == '/products':
            product_id = params.get('id', [''])[0]
            
            response = self.get_webpage()
            
            # Vulnerable part: direct string concatenation for SQL query
            if product_id:
                conn = sqlite3.connect('demo.db')
                cursor = conn.cursor()
                
                # VULNERABLE: No sanitization of input
                query = f"SELECT * FROM Products WHERE name LIKE '%{product_id}%'"
                
                try:
                    response += ("<h2>"
                                 "Vulnerable/Unsanitised SQL query:"
                                 "<code>"
                                 "SELECT * FROM Products WHERE name LIKE '%{product_id}%'"
                                 "</code>"
                                 "</h2>")

                    response += f"<h2>Executing query: <code>{query}</code></h2>"
                    cursor.execute(query)
                    results = cursor.fetchall()
                    
                    if results:
                        response += "<h2>Product Details:</h2>"
                        response += "<table border='1'><tr><th>ID</th><th>Name</th><th>Description</th><th>Price</th></tr>"
                        for row in results:
                            response += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>${row[3]}</td></tr>"
                        response += "</table>"
                    else:
                        response += "<p>No products found.</p>"
                except sqlite3.Error as e:
                    response += f"<p>Error in SQL query: {e}</p>"
                
                conn.close()
            
            # Search form
            response += """
            <h2>Search for a Product</h2>
            <form action="/products" method="get">
                <label for="id">Product ID:</label>
                <input type="text" id="id" name="id">
                <input type="submit" value="Search">
            </form>
            """
        else:
            response = self.get_webpage()
            response += """
            <h1>Welcome to the Vulnerable SQL Demo</h1>
            <p>This server has been created for educational purposes to demonstrate SQL injection.</p>
            <p>Go to the <a href="/products">Products</a> page to start.</p>
            """
        
        self.wfile.write(response.encode())
    
    def get_webpage(self):
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>SQL Injection Demo</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 0; padding: 20px; line-height: 1.6; }
                .container { max-width: 800px; margin: 0 auto; }
                h1 { color: #2c3e50; }
                table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
                th, td { padding: 12px; text-align: left; }
                th { background-color: #2c3e50; color: white; }
                tr:nth-child(even) { background-color: #f2f2f2; }
                .tip { color: #7f8c8d; font-style: italic; }
                form { margin: 20px 0; padding: 20px; background-color: #f9f9f9; border-radius: 5px; }
                input[type="text"] { padding: 8px; width: 200px; margin-right: 10px; }
                input[type="submit"] { padding: 8px 16px; background-color: #2c3e50; color: white; border: none; cursor: pointer; }
                code { background-color: #f9f9f9; padding: 2px 4px; border-radius: 4px; font-family: monospace; }
                .highlight { background-color: #ffe6e6; padding: 15px; border-left: 4px solid #ff5252; margin: 20px 0; }
            </style>
        </head>
        <body>
            <div class="container">
            </div>
        </body>
        </html>
        """

if __name__ == '__main__':
    # Set up the database first
    setup_database()
    
    # Start the server
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, VulnerableHandler)
    print("="*50)
    print("FOR EDUCATIONAL PURPOSE ONLY.")
    print("="*50)
    print('Server running at http://localhost:8000...')
    httpd.serve_forever()
