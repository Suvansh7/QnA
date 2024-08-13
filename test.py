
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


corpus = ""
def next_question(ans,corpus) :
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", convert_system_message_to_human=True,google_api_key="AIzaSyD-WsKQ2O-isAK-PJjFxTusl1-TxcQ8l2E")
    ans = model(
    [
    SystemMessage(content="Only Generate a single line next response relevant to given answer to evaluate the candidate skills, As you are taking an interview"),
    HumanMessage(content=f"Answer - {ans} /n If answer is not worth it to generate question then take refrence of previous answers which are -/n {corpus}"),
    ]
    )
    ques = ans.content
    return ques





print("Tell me about Yourself")
while True:
    ans = input()
    response = next_question(ans, corpus)
    corpus = corpus + "  "  + ans
    print(response)
    

