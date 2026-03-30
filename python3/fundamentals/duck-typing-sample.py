class DropDownController:
    def draw(self):
        print("Draw drop down")


class TextBoxController:
    def draw(self):
        print("Draw text box.")


def draw(controllers):
    for control in controllers:
        control.draw()


drop_down = DropDownController()
text_box = TextBoxController()

draw([text_box, drop_down])
