import mysql.connector as mc
import streamlit as st

def get_db_connection():
    try:
        conn = mc.connect(
            host="localhost",
            user="root",          
            password="Sedhu.k001@",
            database="stock_data"
        )
        return conn
    except mc.Error as e:
        st.error(f"Database connection error: {e}")
        return None

conn = get_db_connection()
st.write(conn)

if conn:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT * FROM sector;
        """
        cursor.execute(query)
        user = cursor.fetchall()
        st.write(user)