import streamlit as st

# Import libraries for text formatting (optional)
from textwrap import indent
import google.generativeai as genai

st.set_page_config(page_title="Film Recommender", page_icon="🍿")


API_KEY = open("api.txt", "r").read().strip()  # Replace with your actual API key

def generate_recommendation(prompt):
  """
  Generates movie recommendations using the generative AI model.
  """
  genai.configure(api_key=API_KEY)  # Configure the API key
  model = genai.GenerativeModel('gemini-pro')  # Specify the model
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
    # You can optionally format the response for better readability (uncomment below)
    # formatted_response = indent(recommendation, '> ', predicate=lambda _: True)
    # st.write(formatted_response)
    st.write(recommendation)


if __name__ == "__main__":
  main()






# st.markdown("# Mapping Demo")
# st.sidebar.header("Mapping Demo")
# st.write(
#     """This demo shows how to use
# [`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
# to display geospatial data."""
# )


# @st.cache_data
# def from_data_file(filename):
#     url = (
#         "http://raw.githubusercontent.com/streamlit/"
#         "example-data/master/hello/v1/%s" % filename
#     )
#     return pd.read_json(url)


# try:
#     ALL_LAYERS = {
#         "Bike Rentals": pdk.Layer(
#             "HexagonLayer",
#             data=from_data_file("bike_rental_stats.json"),
#             get_position=["lon", "lat"],
#             radius=200,
#             elevation_scale=4,
#             elevation_range=[0, 1000],
#             extruded=True,
#         ),
#         "Bart Stop Exits": pdk.Layer(
#             "ScatterplotLayer",
#             data=from_data_file("bart_stop_stats.json"),
#             get_position=["lon", "lat"],
#             get_color=[200, 30, 0, 160],
#             get_radius="[exits]",
#             radius_scale=0.05,
#         ),
#         "Bart Stop Names": pdk.Layer(
#             "TextLayer",
#             data=from_data_file("bart_stop_stats.json"),
#             get_position=["lon", "lat"],
#             get_text="name",
#             get_color=[0, 0, 0, 200],
#             get_size=15,
#             get_alignment_baseline="'bottom'",
#         ),
#         "Outbound Flow": pdk.Layer(
#             "ArcLayer",
#             data=from_data_file("bart_path_stats.json"),
#             get_source_position=["lon", "lat"],
#             get_target_position=["lon2", "lat2"],
#             get_source_color=[200, 30, 0, 160],
#             get_target_color=[200, 30, 0, 160],
#             auto_highlight=True,
#             width_scale=0.0001,
#             get_width="outbound",
#             width_min_pixels=3,
#             width_max_pixels=30,
#         ),
#     }
#     st.sidebar.markdown("### Map Layers")
#     selected_layers = [
#         layer
#         for layer_name, layer in ALL_LAYERS.items()
#         if st.sidebar.checkbox(layer_name, True)
#     ]
#     if selected_layers:
#         st.pydeck_chart(
#             pdk.Deck(
#                 map_style="mapbox://styles/mapbox/light-v9",
#                 initial_view_state={
#                     "latitude": 37.76,
#                     "longitude": -122.4,
#                     "zoom": 11,
#                     "pitch": 50,
#                 },
#                 layers=selected_layers,
#             )
#         )
#     else:
#         st.error("Please choose at least one layer above.")
# except URLError as e:
#     st.error(
#         """
#         **This demo requires internet access.**
#         Connection error: %s
#     """
#         % e.reason
#     )