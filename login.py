import streamlit as st
import pandas as pd
#DB management
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
 
def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS userTable(username TEXT, password TEXT)')

def addUserData(username,password):
    c.execute('INSERT INTO userTable(username,password) Values (?,?)' , (username,password))
    conn.commit()

def loginUser(username,password):
    c.execute('SELECT * FROM userTable WHERE username =? AND password =?',(username,password))
    data = c.fetchall()
    return data

def viewUsers():
    c.execute('SELECT * FROM userTable')
    data = c.fetchall()
    return data

def main():
    st.title("Alvai Youth Club")

    menu = ["Home", "Login", "Signup"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.write("Welcome to main page of the Alavi youth club")
        st.image('alvai.jpg')
    elif choice == "Login":
        st.write("Login in  to the page")
        name = st.sidebar.text_input("User name") 
        password = st.sidebar.text_input("Password", type = 'password')
        if st.sidebar.checkbox("Login"):
            createTable()
            result = loginUser(name,password)
            if result:
                st.success("Logged In as {}".format(name))
                task = st.selectbox('Task',['Add post','Analytics','Profiles'])
                if task == 'Add post':
                    st.subheader("Add the post , regarding their rating")
                elif task == 'Analytics':
                    st.subheader("Analyse the employee's performance")
                elif task == 'Profiles':
                    st.subheader("Check their profile and update")  
                    userResult = viewUsers()
                    clean_db = pd.DataFrame(userResult , columns = ['Username', 'Password'])
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect password")                  
    elif choice == "Signup": 
        if st.button("Start"):
            st.subheader("Create New Account")   
            newUser = st.text_input("Username")
            newPassword = st.text_input('Password',type='password')

            if st.button("SignUp"):
                createTable()
                addUserData(newUser,newPassword)
                st.success(" You have successfully created a valid account")
           # else:
                
 


if __name__ == "__main__":
    main()
     