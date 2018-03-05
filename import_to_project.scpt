on run argv
  tell application "Things3"
    set task_name to item 1 of argv
    set task_notes to item 2 of argv
    set project_name to item 3 of argv

    set newTask to make new to do with properties {name: task_name} at beginning of project project_name
    set notes of newTask to task_notes
    set tag names of newTask to "imported"
  end tell
end run
