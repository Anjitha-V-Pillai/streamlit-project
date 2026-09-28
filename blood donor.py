import mysql.connector
import streamlit as st


class BloodBankDB:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="blood_db",
        )
        self.cursor = self.conn.cursor()

    def add_donor(self, name, blood_group, phone, city, last_donation):
        query = "INSERT INTO donor (name, blood_group, phone, city, last_donation) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(
            query, (name, blood_group, phone, city, last_donation)
        )
        self.conn.commit()

    def get_all_donors(self):
        self.cursor.execute("SELECT * FROM donor")
        return self.cursor.fetchall()

    def get_donor_by_id(self, donor_id):
        self.cursor.execute("SELECT * FROM donor WHERE id = %s", (donor_id,))
        return self.cursor.fetchone()

    def update_donor(
        self, donor_id, name, blood_group, phone, city, last_donation
    ):
        query = "UPDATE donor SET name=%s, blood_group=%s, phone=%s, city=%s, last_donation=%s WHERE id=%s"
        self.cursor.execute(
            query, (name, blood_group, phone, city, last_donation, donor_id)
        )
        self.conn.commit()

    def delete_donor(self, donor_id):
        self.cursor.execute("DELETE FROM donor WHERE id = %s", (donor_id,))
        self.conn.commit()


db = BloodBankDB()

st.title("Blood Donor Management System")

menu = ["Add", "View All", "Search", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add":
    name = st.text_input("Name")
    blood_group = st.selectbox(
        "Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    )
    phone = st.text_input("Phone")
    city = st.text_input("City")
    last_donation = st.date_input("Last Donation Date")
    if st.button("Add Donor"):
        db.add_donor(name, blood_group, phone, city, last_donation)
        st.success("Donor added successfully")

elif choice == "View All":
    records = db.get_all_donors()
    st.table(records)

elif choice == "Search":
    donor_id = st.number_input("Enter ID", min_value=1, step=1)
    if st.button("Search"):
        record = db.get_donor_by_id(donor_id)
        st.write(record)

elif choice == "Update":
    donor_id = st.number_input("Enter ID to Update", min_value=1, step=1)
    name = st.text_input("Name")
    blood_group = st.selectbox(
        "Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    )
    phone = st.text_input("Phone")
    city = st.text_input("City")
    last_donation = st.date_input("Last Donation Date")
    if st.button("Update Donor"):
        db.update_donor(
            donor_id, name, blood_group, phone, city, last_donation
        )
        st.success("Donor updated successfully")

elif choice == "Delete":
    donor_id = st.number_input("Enter ID to Delete", min_value=1, step=1)
    if st.button("Delete Donor"):
        db.delete_donor(donor_id)
        st.success("Donor deleted successfully")