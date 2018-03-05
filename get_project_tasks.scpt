on run argv
  tell application "Things3"
    set project_name to item 1 of argv

    set pr to project project_name
    set tasks to to dos of pr
    set arr to {}

    repeat with tsk in tasks
      set _name to name of tsk
      log _name
    end repeat
  end tell
end run
