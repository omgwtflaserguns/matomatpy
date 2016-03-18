
import npyscreen
import constants


class OptionsDisplay (npyscreen.Form):

    def create(self,):
        self.wgHeader = self.add_widget(npyscreen.MultiLineEdit,
                                        value='No Config found, please edit the following values:',
                                        editable=False)
        self.wgOptions = self.add(npyscreen.OptionListDisplay,
                                  name='Options',
                                  values=self.parentApp.config.options.options,
                                  scroll_exit=True,
                                  max_height=None,
                                  rely=5)

    def afterEditing(self):
        self.parentApp.config.write_config()

        if self.parentApp.config.read_config():
            self.parentApp.initialize()
            self.parentApp.switchForm(constants.Forms.LOGIN_FORM)
