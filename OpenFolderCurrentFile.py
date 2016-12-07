import sublime, sublime_plugin
import os, sys
import subprocess

class OpenFolderCurrentFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if not self.view.file_name():
      return
    folder_name, file_name = os.path.split(self.view.file_name())

    # handle network mounts
    if folder_name[2:4] == '\\\\':
      folder_name = folder_name[0:3] + folder_name[4:]

    # windows
    if 'win' in sys.platform:
      command = "explorer " + folder_name
      subprocess.Popen(command)

    # mac osx
    elif 'darwin' in sys.platform:
      command = "open " + folder_name
      subprocess.Popen(command)