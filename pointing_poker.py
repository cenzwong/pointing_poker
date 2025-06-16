import streamlit as st

# Define the standard Planning Poker values
poker_values = [0, 1, 2, 3, 5, 8, 13, 21, '?', '∞']

# Initialize session state variables
if 'players' not in st.session_state:
    st.session_state.players = []
if 'votes' not in st.session_state:
    st.session_state.votes = {}
if 'voting_complete' not in st.session_state:
    st.session_state.voting_complete = False

# Function to reset the session for a new round of voting
def reset_session():
    st.session_state.votes = {}
    st.session_state.voting_complete = False

# Function to add a player
def add_player(name):
    if name and name not in st.session_state.players:
        st.session_state.players.append(name)

# Function to submit a vote
def submit_vote(name, vote):
    if name in st.session_state.players:
        st.session_state.votes[name] = vote
        if len(st.session_state.votes) == len(st.session_state.players):
            st.session_state.voting_complete = True

# Streamlit app layout
st.title("Planning Poker")

# Player name input
name = st.text_input("Enter your name:")
if st.button("Join Session"):
    add_player(name)

# Display players
st.subheader("Players")
for player in st.session_state.players:
    st.write(player)

# Voting section
if name in st.session_state.players:
    st.subheader("Vote on Story Points")
    vote = st.selectbox("Select your vote:", poker_values)
    if st.button("Submit Vote"):
        submit_vote(name, vote)

# Display votes if voting is complete
if st.session_state.voting_complete:
    st.subheader("Votes")
    for player, vote in st.session_state.votes.items():
        st.write(f"{player}: {vote}")

    if st.button("Reset Session"):
        reset_session()
