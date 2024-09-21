import sublime_plugin


class ToggleCaseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Iterate over selected text
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)

                # check if the text is all uppercase or lowercase, then toggle.
                # To simplify logic, just check if everything is lower, if so then
                # uppercase, otherwise lowercase (as that's usually what I prefer).
                if selected_text.islower():
                    self.view.replace(edit, region, selected_text.upper())
                else:
                    self.view.replace(edit, region, selected_text.lower())
