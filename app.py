import streamlit as st
import random

st.title("🎲 Guess the Number Game!")

# Initialize session state variables
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        if guess < st.session_state.number_to_guess:
            st.info("🔵 Too low! Try a higher number.")
        elif guess > st.session_state.number_to_guess:
            st.info("🔴 Too high! Try a lower number.")
        else:
            st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!")
            st.balloons()
            st.session_state.game_over = True

# Restart the game
if st.button("Restart Game"):
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.experimental_rerun()
