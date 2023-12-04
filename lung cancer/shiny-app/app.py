from shiny import *
from pathlib import Path
import matplotlib.pyplot as plt
from predict import pred, query
from htmltools import tags
from helper_text import info_modal
# from shinywidgets import output_widget
# import shiny.experimental as x

app_ui = ui.page_navbar(
    ui.nav(
        "By BMI Group 3. 14/11/2023",
        ui.div(
            {"class": "card mb-3"},
            ui.div(
                {"class": "card-body"},
                ui.h6({"class": "card-title mt-0"}, "Please fill in your information below."),
            ),
            ui.div(
                {"class": "card-footer"},
                ui.input_select("x1", "Gender", ['Male','Female']),
                ui.input_numeric("x2", "Age", value=25),
                ui.input_slider("x3", "How frequent do you smoke? 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
                ui.input_radio_buttons("x4", "Do you have yellow fingers?", {"a": "No", "b": "Yes"}),
                ui.input_slider("x5", "Do you feel peer pressure? 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
                ui.input_slider("x6", "Do you feel anxious? 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
                ui.input_radio_buttons("x7", "Do you have any chronic disease?", {"a": "No", "b": "Yes"}),
                ui.input_slider("x8", "Do you feel fatigue? 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
                ui.input_radio_buttons("x9", "Have you had any allergic reactions recently", {"a": "No", "b": "Yes"}),
                ui.input_radio_buttons("x10", "Do you wheeze sometimes?", {"a": "No", "b": "Yes"}),
                ui.input_slider("x11", "How frequent do you take alcohol? 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
                ui.input_radio_buttons("x12", "Do you cough recently?", {"a": "No", "b": "Yes"}),
                ui.input_slider("x13", "Do you feel breath shortness? 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
                ui.input_radio_buttons("x14", "Do you have swallowing difficulty?", {"a": "No", "b": "Yes"}),
                ui.input_radio_buttons("x15", "Do you feel chest pain recently?", {"a": "No", "b": "Yes"}),
            ),
        ),
                ui.div(
                    {"class": "card mb-3"},
                    ui.div(
                        {"class": "card-body"},
                        ui.h3({"class": "card-title mt-0"}, "Evaluation"),
                        ui.h6("Once finish filling the information below, click 'Finsh' to view your report. \n"),
                        ui.input_action_button("btn", "Finish"),
                    ),
                    ui.div(
                        {"class": "card-footer"},
                        tags.h3("Evaluation result: "),
                        ui.output_text_verbatim("txt", placeholder=True),
                        ui.tags.hr(),
                        tags.h3("Suggestions"),
                        tags.h6('(Please wait for several seconds before ChatGpt finish its generation.)\n'),
                        ui.output_text("txt_gpt"),
                    ),
                ),
                ui.div(
                    {"class": "card"},
                    ui.div(
                        {"class": "card-body"},
                        ui.h1({"class": "card-title m-0"}, "Analysis"),
                    ),
                    ui.div(
                        {"class": "card-body overflow-auto pt-0"},
                        tags.h2("Model performance:"),
                        ui.img(src="score.png",height = 143, width = 434),
                        tags.h2("\n"),
                        tags.h2("Correlation heatmap:"),
                        ui.img(src="heatmap.png",height = 366, width = 594),
                    ),
                ),
    ),
)

# A ReactiveVal which is shared across all sessions.
shared_val = reactive.Value(None)

def server(input: Inputs, output: Outputs, session: Session):
    # This observer watches n, and changes shared_val, which is shared across all running sessions.
    info_modal()
    @reactive.Effect
    @reactive.event(input.info_icon)
    def _():
        info_modal()

    @output
    @render.text
    @reactive.event(input.btn)
    def txt():
        eval, level, _ = final_results()
        return eval

    @output
    @render.text
    @reactive.event(input.btn)
    def txt_gpt():
        _, _, response = final_results()
        return response

    def final_results():
        Gender = [1 if input.x1()=='Male' else 0][0]
        Age = int(input.x2())
        Smoke = 1+input.x3()/4
        Yellow_finger = [1 if input.x4()=='a' else 2][0]
        Anxiety = 1+input.x5()/4
        Peer_pressure = 1+input.x6()/4
        Chronic_Disease = [1 if input.x7()=='a' else 2][0]
        Fatigue = 1+input.x8()/4
        Allergy = [1 if input.x9()=='a' else 2][0]
        Wheeze = [1 if input.x10()=='a' else 2][0]
        Alcohol = 1+input.x11()/4
        Coughing = [1 if input.x12()=='a' else 2][0]
        Breath_Shortness = 1+input.x13()/4
        Swallowing_Difficulty = [1 if input.x14()=='a' else 2][0]
        Chest_pain = [1 if input.x15()=='a' else 2][0]
        pred_value = round(float(pred(Gender,Age,Smoke,Yellow_finger,Anxiety,Peer_pressure,Chronic_Disease,Fatigue,Allergy,Wheeze,Alcohol,Coughing,Breath_Shortness,Swallowing_Difficulty,Chest_pain)[0][1]),4)
        level = pred_level(pred_value)
        Smoke_cond, Alcohol_cond = map_language(Smoke, Alcohol)
        response = query(Smoke_cond, Alcohol_cond, level)
        def s(level):
            if level == 'Low risk': return 'You have a good habit towards low lung cancer risk. Please keep it up!'
            elif level == 'High risk': return 'Please note that it\'s better for you to seek medical attention immediately.'
            else: return 'You are currently at low to medium risk for lung cancer. \nIf you feel unwell, please consult your doctor.'

        return s(level), level, response
    
    def map_language(Smoke, Alcohol) -> str:
        if Smoke >= 1.5: Smoke_cond = 'frequently smoke,'
        elif Smoke >= 1.25: Smoke_cond = 'seldom smoke,'
        else: Smoke_cond = 'never smoke,'

        if Alcohol>= 1.5: Alcohol_cond = 'frequently take alcohol,'
        elif Alcohol>= 1.25: Alcohol_cond = 'seldom take alcohol,'
        else: Alcohol_cond = 'never take alcohol,'

        return Smoke_cond, Alcohol_cond


    def pred_level(pred_value: float) -> str:
        if pred_value < 0.4:
            return 'Low risk'
        elif pred_value > 0.8:
            return 'High risk'
        else:
            return 'Medium risk'


www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)