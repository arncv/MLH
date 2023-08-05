from taipy.gui import Gui

value = 10

page = """
#Our Very First Taipy Application

Slider value: <|{value}|> <br/>
<|{value}|slider|>

"""

Gui(page).run(use_reloader=True, port=5001)