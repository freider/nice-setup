# coding: utf8
import sublime_plugin
import subprocess
import os
import sys

print "Loading NiceSetup™"


def debug(message):
    print >> sys.stderr, "NiceSetup:", message


class CommandOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
#        settings = view.settings()
#        folders = settings.get("commands")
        print
        test_dir = view.file_name()
        nice_setup_file = None
        while test_dir != '/':
            test_file = os.path.join(test_dir, ".nicesetup")
            if os.path.exists(test_file):
                nice_setup_file = test_file
                break
            test_dir = os.path.dirname(test_dir)
        if not nice_setup_file:
            debug("No .nicesetup file found in parent dirs")
            return
        debug("Found {nice_setup_file}".format(**locals()))
        local_dir = os.path.dirname(nice_setup_file)
        with open(nice_setup_file) as f:
            remote_location = f.read().strip()
        debug("Sync location {remote_location}".format(**locals()))

        cmd = ['rsync', '-av', '--delete', local_dir, remote_location]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout:
            debug(line.rstrip('\n'))
        p.wait()
        print
