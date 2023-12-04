from shiny.ui import modal_show, modal, modal_button
from htmltools import TagList, tags
from shiny import ui, module, reactive

# @module.ui
# def map_ui():
#     return ui.tags.div(
#         ui.tags.div(
#             about_text,
#             ui.tags.hr(),
#             slider_text_map,
#             ui.tags.br(),
#             ui.input_slider(
#                 id="years_value",
#                 label="Select Year",
#                 min=1990,
#                 max=2017,
#                 value=2010,
#                 sep="",
#             ),
#             ui.tags.hr(),
#             dataset_information,
#             ui.tags.hr(),
#             missing_note,
#             class_="main-sidebar card-style",
#         ),
#         ui.tags.div(
#             output_widget("map", width="auto", height="auto"),
#             class_="main-main card-style no-padding",
#         ),
#         class_="main-layout",
#     )

# about_text = TagList(
#     tags.h3("About"),
#     tags.br(),
#     tags.p(
#         """
#         The app gives a visual overview of PM2.5 air pollution
#         for different
#         countries over the years and its potential relationship
#         to respiratory
#         diseases and their prevalence.
#         """,
#         style="""
#         text-align: justify;
#         word-break:break-word;
#         hyphens: auto;
#         """,
#     ),
# )

# slider_text_map = tags.p(
#     """
#     Please use the slider below to choose the year. The map will
#     reflect data for the input
#     """,
#     style="""
#     text-align: justify;
#     word-break:break-word;
#     hyphens: auto;
#     """,
# )

# slider_text_plot = tags.p(
#     """
#     Please use the slider below to change the years as well as the
#     dropdown to select the countries to compare. By default, the mean
#     data for the World is plotted.
#     """,
#     style="""
#     text-align: justify;
#     word-break:break-word;
#     hyphens: auto;
#     """,
# )

dataset_information = TagList(
    tags.strong(tags.h3("Dataset Information")),
    tags.p(
        """
        The data is from the East-China Institute of Technology(ECIT).
        Regarding the prevalence rate, we relied on
        Singapore Cancer Registry Annual Report. References
        can be found below.
        """,
        style="""
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
    tags.ul(
        tags.li(
            tags.a(
                "ECIT",
                href=(
                    "https://doi.org/10.1016/0031-3203(91)90074-F"
                    + ""
                ),
            )
        ),
        tags.li(
            tags.a(
                "SG Annual Report",
                href=(
                    "https://www.nrdo.gov.sg/docs/librariesprovider3/default-document-library/0"
                    + "scr-ar-2021-web-report.pdf?sfvrsn=591fc02c_"
                ),
            )
        ),
    ),
)

missing_note = TagList(
    tags.p(
        tags.strong("Note: "),
        """
        This website is only designed for **NUS BMI5101 Group3** project. 
        All content on this page is for reference only.
        """,
        style="""
        font-size: 14px;
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)


def info_modal():
    modal_show(
        modal(
            tags.strong(tags.h3("Lung cancer self-evaluation")),
            tags.p(
                "Exploring relationships between symptom, lifestyle & Lung cancer"
            ),
            tags.hr(),
            tags.strong(tags.h4("Problem Statement")),
            tags.p(
                """
            Lung cancer is the third most common cancer in Singapore and is often only diagnosed 
            at the late-stage. We would like to increase the awareness in the 
            general population by a self-evaluated platform to provide advice through ChatGPT.
            """,
                style="""
            text-align: justify;
            word-break:break-word;
            hyphens: auto;
            """,
            ),
            tags.hr(),
            dataset_information,
            tags.hr(),
            missing_note,
            size="l",
            easy_close=True,
            footer=modal_button("Close"),
        )
    )

def questions():
    ui.nav('Lung cancer',
        ui.input_select("x1", "Gender", ['Male','Female']),
        ui.input_date("x2", "Date of birth"),
        ui.input_slider("x3", "How frequent do you smoke?\n 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
        ui.input_radio_buttons("x4", "Do you have yellow fingers?", {"a": "No", "b": "Yes"}),
        ui.input_slider("x5", "Do you feel peer pressure?\n 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
        ui.input_slider("x6", "Do you feel anxious?\n 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
        ui.input_radio_buttons("x7", "Do you have any chronic disease?", {"a": "No", "b": "Yes"}),
        ui.input_slider("x8", "Do you feel fatigue?\n 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
        ui.input_radio_buttons("x9", "Have you had any allergic reactions recently", {"a": "No", "b": "Yes"}),
        ui.input_radio_buttons("x10", "Do you wheeze sometimes?", {"a": "No", "b": "Yes"}),
        ui.input_slider("x11", "How frequent do you take alcohol?\n 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
        ui.input_radio_buttons("x12", "Do you cough recently?", {"a": "No", "b": "Yes"}),
        ui.input_slider("x13", "Do you feel breath shortness?\n 0-Never 1-Seldom 2-Often 3-Frequent 4-Everyday", value=0, min=0, max=4),
        ui.input_radio_buttons("x14", "Do you have swallowing difficulty?", {"a": "No", "b": "Yes"}),
        ui.input_radio_buttons("x15", "Do you feel chest pain recently?", {"a": "No", "b": "Yes"}),
    )