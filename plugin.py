import os
import subprocess
import sublime_plugin


class ZzCoqFormatCommand(sublime_plugin.TextCommand):

    """zz_coq_format"""

    def run(self, edit):
        full_path = self.view.file_name()
        if full_path:
            file_base_name = os.path.basename(full_path)
            file_name, file_name_extension = os.path.splitext(file_base_name)
            print(file_name)
            print(file_name_extension)
            if not file_name_extension == ".v":
                print(str(full_path) + ": not vernacular file")
                return
        else:
            print(str(full_path) + ": not a file")
            return

        print(full_path)
        output = subprocess.Popen(['coqc', '-beautify', full_path], stdout=subprocess.PIPE)
        if output.communicate()[1]:
            print(output.communicate()[1])
        output = subprocess.Popen(['mv', full_path+".beautified", full_path],
                                  stdout=subprocess.PIPE)
        if output.communicate()[1]:
            print(output.communicate()[1])
