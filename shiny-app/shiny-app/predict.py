import pandas as pd
import joblib

def pred(Gender,Age,Smoke,Yellow_finger,Anxiety,Peer_pressure,Chronic_Disease,Fatigue,Allergy,Wheeze,Alcohol,Coughing,Breath_Shortness,Swallowing_Difficulty,Chest_pain):
    dic = {'GENDER': Gender, 'AGE': Age, 'SMOKING':Smoke, 'YELLOW_FINGERS':Yellow_finger,'ANXIETY':Anxiety,'PEER_PRESSURE':Peer_pressure,
           'CHRONIC DISEASE':Chronic_Disease,'FATIGUE ':Fatigue,'ALLERGY ':Allergy,'WHEEZING':Wheeze,'ALCOHOL CONSUMING':Alcohol,
           'COUGHING':Coughing,'SHORTNESS OF BREATH':Breath_Shortness,'SWALLOWING DIFFICULTY':Swallowing_Difficulty,'CHEST PAIN':Chest_pain}
    test_data = pd.DataFrame(dic, index=[0])
    ensemble = joblib.load('saved_model/ensemble_1.pkl')
    preds = ensemble.predict_proba(test_data)
    return preds

def query(Smoke:str, Alcohol: str, level: str) -> str:
    # import requests
    # API_URL = "https://api-inference.huggingface.co/models/Locutusque/gpt2-large-medical"
    # headers = {"Authorization": "Bearer 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"}
    # payload = {
    #     "inputs": f"<|USER|> One {Smoke}and {Chronic_Disease} and his lung cancer risk is {level}. Doctor's advice for him are \n <|ASSISTANT|>",
    # "parameters":{
    #     "max_new_tokens":100,
    #     "return_full_text":True,
    #     }
    # }
    
    # response = requests.post(API_URL, headers=headers, json=payload).json()[0]['generated_text'].split('<|ASSISTANT|>')[-1]
    # return 'Thank you for your consultation! Based on the your given information, you should '+response
    import openai
    openai.api_key="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"
    template = f"""
    <|PATIENT|> One {Smoke} and {Alcohol} and his lung cancer risk is {level}. Doctor's advice for him are
    <|ASSISTANT|>
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = 0,
        messages=[
        {"role": "system", "content": f"You are a good doctor for lung cancer, give concise advice and guideline to help patient\
         who {Smoke} and {Alcohol} and his lung cancer risk is {level} within 120 words. Use line break sign to make your answer cleaner."},
        {"role": "assistant", "content": "Sure, I am so glad to give advices and any help you want!"},
        {"role": "user", "content": "{template}"},
        ],
    )

    return 'Thank you for your consultation! ' + response['choices'][0]['message']['content']
        

if __name__== "__main__":
    # res = pred(0,59,1,1,1,2,1,2,1,2,1,2,2,1,2)[0][1]
    # print(round(float(res),4))
    print(query('Frequently smoke,', 'have chronic disease,', 'medium risk'))

