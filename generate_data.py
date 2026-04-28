import sqlite3
import random
from datetime import datetime, timedelta

def create_database():
    conn = sqlite3.connect('fi_money_clone.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        signup_date DATE,
        status TEXT,
        acquisition_channel TEXT
    )
    ''')

    # Create Transactions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        transaction_date DATE,
        amount DECIMAL(10, 2),
        transaction_type TEXT,
        revenue DECIMAL(10, 2),
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
    ''')

    # Generate synthetic data
    # 1. Generate users
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    days_range = (end_date - start_date).days

    users = []
    for i in range(1, 1001): # 1000 users
        signup_date = start_date + timedelta(days=random.randint(0, days_range))
        status = random.choices(['active', 'inactive'], weights=[0.8, 0.2])[0]
        channel = random.choice(['Organic', 'Referral', 'Paid Ads'])
        users.append((i, signup_date.strftime('%Y-%m-%d'), status, channel))

    cursor.executemany('INSERT INTO users VALUES (?, ?, ?, ?)', users)

    # 2. Generate transactions
    transactions = []
    transaction_id = 1
    
    transaction_types = ['deposit', 'withdrawal', 'transfer', 'bill_payment']
    
    for user in users:
        user_id = user[0]
        signup_date = datetime.strptime(user[1], '%Y-%m-%d')
        
        # Determine number of transactions based on status
        num_transactions = random.randint(5, 50) if user[2] == 'active' else random.randint(1, 5)
        
        for _ in range(num_transactions):
            # Transactions must happen after signup
            txn_days_after_signup = random.randint(0, (end_date - signup_date).days)
            txn_date = signup_date + timedelta(days=txn_days_after_signup)
            
            txn_type = random.choice(transaction_types)
            amount = round(random.uniform(10.0, 5000.0), 2)
            
            # Assuming revenue is generated from fees on transfers and bill payments
            revenue = 0
            if txn_type in ['transfer', 'bill_payment']:
                revenue = round(amount * 0.01, 2) # 1% fee
                
            transactions.append((transaction_id, user_id, txn_date.strftime('%Y-%m-%d'), amount, txn_type, revenue))
            transaction_id += 1

    cursor.executemany('INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?)', transactions)

    conn.commit()
    conn.close()
    print("Database created and synthetic data inserted successfully.")

if __name__ == '__main__':
    create_database()
