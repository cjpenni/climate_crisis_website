import datetime
import streamlit as st
import os

# Function to read the list of discussion boards from a text file
def read_existing_boards():
    if os.path.exists("discussion_boards.txt"):
        with open("discussion_boards.txt", "r") as f:
            existing_boards = f.read().splitlines()
        return existing_boards
    else:
        return []

# Function to write the list of discussion boards to a text file
def write_existing_boards(existing_boards):
    with open("discussion_boards.txt", "w") as f:
        for board in existing_boards:
            f.write(board + "\n")

st.set_page_config(page_title="Discussion Boards", page_icon="📊")

# Define the list of existing discussion boards
existing_boards = read_existing_boards()

# Function to handle discussion page
def discussion_page(board_name):
    st.title(f"{board_name} Discussion Board")

    # Get file path for the discussion text file of the current board
    file_path = os.path.join("discussions", f"{board_name.lower().replace(' ', '')}_discussion.txt")

    # add a key to the text_input and text_area widgets
    name = st.text_input("Enter your name:", key=f"{board_name}_name")

    new_message = st.text_area("Enter your message:", key=f"{board_name}_new_message")

    submit_button = st.button("Submit")

    if submit_button:
        if new_message:
            with open(file_path, "a") as f:
                # Get the current timestamp
                timestamp = datetime.datetime.now().strftime("%I:%M:%S %p %m/%d/%Y")
                f.write(f"{timestamp} - {name}: {new_message}\n")
            new_message = ""  # Clear the text area after submitting
            st.session_state[f'{board_name}_message_submitted'] = True  # Store a flag to indicate a message was submitted

    st.header("Discussion")

    # Display the discussion messages
    with open(file_path, "r") as f:
        messages = f.readlines()
        for message in messages:
            st.write(message)

# Main discussion board page
def main():
    st.title("Discussion Boards")

    # Add a selectbox to choose which discussion board to view/add to
    default_board = st.session_state.get('new_board', "Add New Board")
    board_name = st.selectbox("Select a discussion board", existing_boards + ["Add New Board"], index=existing_boards.index(default_board) if default_board in existing_boards else len(existing_boards))

    # If the user selects "Add New Board"
    if board_name == "Add New Board":
        new_board_name = st.text_input("Enter the name of the new board:")
        if new_board_name.strip() != "":
            # Add the new board to the list of existing boards
            existing_boards.append(new_board_name)
            # Write the updated list of boards to the text file
            write_existing_boards(existing_boards)
            # Create a new text file for the new board
            with open(os.path.join("discussions", f"{new_board_name.lower().replace(' ', '')}_discussion.txt"), "w") as f:
                st.write("")
            # Display a success message
            st.success(f"New board '{new_board_name}' added successfully!")
            # Store the new board name in the session state
            st.session_state['new_board'] = new_board_name
            # Rerun the script from the top
            st.experimental_rerun()
            

    if board_name != "Add New Board":
        # Display the discussion page for the selected board
        discussion_page(board_name)

main()