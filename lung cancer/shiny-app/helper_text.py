from shiny.ui import modal_show, modal, modal_button
from htmltools import TagList, tags
from shiny import ui, module, reactive

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
