import streamlit as st
import requests

def get_recommendations(user_id):
    # Replace with your actual Azure Function URL
    function_url = "https://myrecommenderfunctionappserverless.azurewebsites.net/api/recommend_article"
    params = {"userID": user_id}
    response = requests.get(function_url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return "Error fetching recommendations"

def main():
    st.title("Article Recommendations")
    user_id = st.text_input("Enter User ID:")
    if st.button("Get Recommendations"):
        if user_id:
            recommendations = get_recommendations(user_id)
            st.write(recommendations)
        else:
            st.warning("Please enter a User ID.")

if __name__ == "__main__":
    main()
