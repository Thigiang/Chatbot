import openai
import streamlit as st
from streamlit_chat import message
# from api_key import openai_secret_key
openai.api_key=st.secrets["api_secret"]



# generate the response function using openai.Completion
# Use this link for hyperparameter reference:
# https://platform.openai.com/docs/api-reference/edits/create


def generate_response(prompt):
    response=openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,stop=None,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    response=response.choices[0]['text']
    return response


# Use streamlit to create chatbox interface

#create the title, use this link to learn more about the parameter in st.tile
#https://docs.streamlit.io/library/api-reference/text/st.title
st.title(":robot_face: :blue[AskMe]:question:")

#store the chat use the key 'generated': response and 'past': question
if 'generated' not in st.session_state:
    st.session_state["generated"]=[]
if "past" not in st.session_state:
    st.session_state["past"]=[]


def updateinput():
    output=generate_response(st.session_state.input)
    # append user_input and output to state
    st.session_state['past'].append(st.session_state.input)
    st.session_state['generated'].append(output)


if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"])-1,-1,-1):
        message(st.session_state["past"][::-1][i], is_user=True, key=str(i)+'_user')
        message(st.session_state["generated"][::-1][i],key=str(i))

user_input = st.text_input("Hello, I am a chatbot. Ask me a question: ","", key="input", on_change=updateinput)