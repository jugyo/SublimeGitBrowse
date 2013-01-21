import sublime, sublime_plugin
import os
import commands
import webbrowser

class CgitBrowseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.settings().get('cgit') == None\
                or self.view.settings().get('cgit').get('base_url') == None:
            sublime.message_dialog("settings for cgit does not exists")

        base_url                = self.view.settings().get('cgit').get('base_url')
        project_dir             = sublime.active_window().folders()[0]
        file_name               = self.view.file_name()
        file_name_from_project  = file_name.replace(project_dir, '')
        branch                  = commands.getoutput("git rev-parse --abbrev-ref HEAD")
        (row, col)              = self.view.rowcol(self.view.sel()[0].end())
        url                     = base_url + '/tree' + file_name_from_project + '?h=' + branch + '#n' + str(row + 1)

        webbrowser.open(url)
