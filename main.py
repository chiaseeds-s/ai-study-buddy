import streamlit as st
import openai

# Page settings
st.set_page_config(page_title="AI Study Buddy", layout="centered")

# Use the OpenAI API key from the Replit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("📚 AI Study Buddy")
st.write("Ask me anything about your subjects like DBMS, OS, DSA, CN, and more!")

# Input box for user's question
user_input = st.text_area("Your Question", placeholder="e.g. What is normalization in DBMS?")

# Button to send the question
if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                # Use OpenAI Chat API to get a response
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful tutor for Computer Science students."},
                        {"role": "user", "content": user_input}
                    ]
                )
                # Show the answer
                answer = response.choices[0].message.content.strip()
                st.success("Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {e}")
