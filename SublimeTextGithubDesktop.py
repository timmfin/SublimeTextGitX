import locale
import os
import subprocess
import sublime, sublime_plugin

class GitDesktopCommand():
    def get_path(self):
        if self.window.active_view():
            return self.window.active_view().file_name()
        elif self.window.folders():
            return self.window.folders()[0]
        else:
            sublime.status_message(__name__ + ': No place to open github to')
            return False

class GithubDesktopOpenCommand(sublime_plugin.WindowCommand, GitDesktopCommand):
    def is_enabled(self):
        return True

    def run(self, *args):
        path = self.get_path()
        if not path:
            return
        if os.path.isfile(path):
            path = os.path.dirname(path)

        settings = sublime.load_settings('Base File.sublime-settings')
        github_desktop_path = settings.get('github_desktop_path', '/usr/local/bin/github')
        if not os.path.isfile(github_desktop_path):
            mac_path = '/Applications/GitHub Desktop.app'
            if os.path.isdir(mac_path):
                github_desktop_path = mac_path + "/Contents/MacOS/github_cli"
            else:
                github_desktop_path = None

        if github_desktop_path in ['', None]:
            sublime.error_message(__name__ + ': github desktop executable path not set, incorrect or no github?')
            return False

        try:
            encoding = locale.getpreferredencoding(do_setlocale=True) or 'UTF-8'
            subprocess.Popen([github_desktop_path], cwd=path.encode(encoding), shell=True)
        except Exception as e:
            sublime.error_message(__name__ + ' Error launching github desktop ' + e.message)
