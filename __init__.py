from mycroft import MycroftSkill, intent_file_handler


class DeezerControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.deezer.intent')
    def handle_control_deezer(self, message):
        self.speak_dialog('control.deezer')


def create_skill():
    return DeezerControl()

