#!/usr/bin/env python

import sys
import subprocess
import csv

# NOTE: This does not work for "Inbox" because it is not a "project" as far as
# Things is concerned. I find the distinction very odd from an API perspective,
# but oh well. If I knew just a little bit more AppleScript I'm sure I could add
# a conditional within `get_project_tasks.scpt`. For now however it won't
# through an error so the import runs just fine. The risk is only of
# duplication, since this function is responsible for getting the set of all
# exisdting task names.
def get_project_tasks(name):
    output = subprocess.getoutput('osascript get_project_tasks.scpt "{}"'.format(name))
    return set(str.split(output, '\n'))

# Not sure if this was specific to me or what, but the export from 2Do included
# some very odd column names in the exported CSV
TASK_KEY = u'\ufeffTASK'
NOTE_KEY = ' NOTE'

# NOTE: The inbox is a special case because I don't know how to do conditional
# logic in AppleScript and I don't care to find out right now.
def add_task_to_project(task, project):
    """
    Import a task into a project or the inbox.
    """

    # See NOTE
    if project == 'Inbox':
        script = './import_to_inbox.scpt'
    else:
        script = './import_to_project.scpt'

    output = subprocess.getoutput('osascript {script} "{name}" "{note}" "{project}"'
            .format(script=script, name=task['name'], note=task['note'], project=project))
    print(output)

def get_tasks_from_csv(csvpath, project):
    """
    Given a CSV return a list of task. Currently only names and notes are
    returned.
    """
    with open(csvpath, newline='') as f:
        reader = csv.DictReader(f)
        result = []
        existing = get_project_tasks(project)

        for row in reader:
            name = row[TASK_KEY]
            note = row[NOTE_KEY]
            if name in existing:
                print('[WARNING]: "{}" already found. Skipping.'.format(name))
            else:
                result.append({ 'name': name, 'note': note })

        return result


def main(argv):
    filepath = argv[1]
    project = argv[2]
    for task in get_tasks_from_csv(filepath, project):
        print('[ADD]: {}'.format(task['name']))
        add_task_to_project(task, project)

if __name__ == '__main__':
    main(sys.argv)
