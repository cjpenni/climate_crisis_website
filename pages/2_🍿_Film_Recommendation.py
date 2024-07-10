import streamlit as st

# Import libraries for text formatting
from textwrap import indent
import google.generativeai as genai

st.set_page_config(page_title="Film Recommender", page_icon="🍿")


API_KEY = open("api.txt", "r").read().strip()  

def generate_recommendation(prompt):
  """
  Generates movie recommendations using the generative AI model.
  """
  genai.configure(api_key=API_KEY)  
  model = genai.GenerativeModel('gemini-pro')  
  response = model.generate_content(prompt)
  return response.text

def main():
  st.title("Film Recommender ")

  liked_movies = st.text_input("Enter the films you liked separated by commas")
  disliked_movies = st.text_input("Enter the films you disliked separated by commas")

  if st.button("Get Recommendations"):
    prompt = f"I liked movies like {liked_movies}. I disliked movies like {disliked_movies}. Can you recommend some ecocinema movies I might enjoy?"
    recommendation = generate_recommendation(prompt)

    st.write(f"Here are some films you might like based on your preferences:")

    st.write(recommendation)


if __name__ == "__main__":
  main()

