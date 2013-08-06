import sublime, sublime_plugin
import os
import commands
import webbrowser
import re

class GitBrowseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.settings().get('cgit') == None\
                or self.view.settings().get('cgit').get('url') == None:
            sublime.message_dialog("settings for cgit does not exists")

        url   = self.view.settings().get('cgit').get('url')

        dir_path = sublime.active_window().folders()[0]

        dir_name = os.path.basename(dir_path)
        url = re.sub(r':dir', dir_name, url)

        file_path  = self.view.file_name().replace(dir_path + '/', '')
        url = re.sub(r':file', file_path, url)

        branch     = commands.getoutput("git rev-parse --abbrev-ref HEAD")
        url = re.sub(r':branch', branch, url)

        (row, col) = self.view.rowcol(min(self.view.sel()[0].begin(), self.view.sel()[0].end()))
        url = re.sub(r':line', str(row + 1), url)

        webbrowser.open(url)
