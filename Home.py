import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# Film and the Climate Crisis")

#st.sidebar.success("Select a demo above.")

st.markdown(
    """
    The point of this website is to create an accessible and 
    informative platform for individuals interested in exploring
    the climate crisis through film.
    ### What is included in this website?
    - Curated film repository
    - Expert analyses
    - Film recommendation system
    - Discussion boards
    ### How do I access these features?
    👈 Select a feature from the sidebar
"""
)
st.markdown("---")

st.write('Please help us keep this website up-to-date by reporting any issues or inaccuracies or features to be added.')
st.link_button("Report form", "https://forms.gle/h3F42z6LwZBq4Cn46")

st.write('Disclaimer: Most of the content on this website was provided by chatbots such as ChatGPT and Google Gemini. Hallucinations were mitigated, but some may still be present.')



    # Streamlit is an open-source app framework built specifically for
    # Machine Learning and Data Science projects.
    # **👈 Select a demo from the sidebar** to see some examples
    # of what Streamlit can do!
    # ### Want to learn more?
    # - Check out [streamlit.io](https://streamlit.io)
    # - Jump into our [documentation](https://docs.streamlit.io)
    # - Ask a question in our [community
    #     forums](https://discuss.streamlit.io)
    # ### See more complex demos
    # - Use a neural net to [analyze the Udacity Self-driving Car Image
    #     Dataset](https://github.com/streamlit/demo-self-driving)
    # - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)