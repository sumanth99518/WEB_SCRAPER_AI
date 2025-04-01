import mesop as me

ROOT_BOX_STYLE = me.Style(
    background="#DFE8E6",
    height="10%",
    font_family="Quicksand",
    display="flex",
    flex_direction="column",
    width="min(100%, 100%)",
    margin=me.Margin.symmetric(
    vertical="auto",
    horizontal="auto",
    ),
    text_align="center",
    align_items="center",
    font_size=60,
    color="#A0430A",

)
INPUT_WINDOW_STYLE =me.Style(


            width="100%",
            height="100%",
            
            font_size="16px",
            background="#f8f8f8",
            color="#000",
            box_shadow="0 2px 4px rgba(0, 0, 0, 0.1)",
            outline="none",  # Remove default browser outline
            font_family="Arial, sans-serif",
        border=me.Border.all(me.BorderSide(width=2, color="#fffff", style="solid")),
)

INPUT_BOX= me.Style(
            margin=me.Margin(top=50,left=150),
            width="80%",
)
ROOT_BOX_STYLE_1 = me.Style(
    background="#DFE8E6",
    height="100%",
    font_family="Quicksand",
    display="flex",
    flex_direction="column",
    width="min(50%, 100%)",
    margin=me.Margin(
        top=50,
        left=350,
        bottom=350
    ),
    text_align="center",
    align_items="center",
    color="#A0430A",

)