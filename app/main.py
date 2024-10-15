import streamlit as st
from openai import OpenAI
from dataclasses import dataclass

client = OpenAI()

@dataclass
class User:
    weight: int


def chat_completion(user: User) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"If i weight {user.weight} pounds and i am doing an endurance activity, how many grams of carbs per hour should i consume?",
            },
        ],
    )

    return completion.choices[0].message.content


def user_info_input() -> User:
    weight = st.number_input(
        "Enter your weight [lbs]",
        min_value=50,
        max_value=400,
        value=200,
    )

    return User(weight)


def main():
    st.set_page_config(
        page_title="SPX Indurance Fuel",
        page_icon="🏃‍♀️",
        layout="centered",
    )

    st.markdown(
        """
    # SPX Endrance Fuel 
    
    ## Nutrition advice intelligence
    """
    )

    user = user_info_input()
    
    advice = ""

    if st.button("Run"):
        with st.spinner("Calculating nutrition plan"):
            advice = chat_completion(user)
            
    st.markdown(advice)
            


if __name__ == "__main__":
    main()
