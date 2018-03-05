# Things 3 2Do Importer

This preject used a combination of Python and Things' AppleScript API to import tasks from a CSV file exported from 2Do.app.

## Export all your tasks one list at a time

Open 2Do and go to `File > Export to CSV...`. That will bring you to this screen:

![Export Dropdown](https://dropsinn.s3.us-west-1.amazonaws.com/2018-03-04%20at%208.54%20PM.png)

Check one list and export the CSV somewhere on your computer.

**NOTE:** It's important that you only export one list at a time if you care about preserving your lists. If not, you can simply export everything and import it all into either the Things Inbox or a specific project.

## Usage

```
./main.py <FILE> <LIST>
```

All tasks will be imported with the #imported tag so you know which tasks came from this script.

#### Import into a specific project

Example: If I exported my Reading List from 2Do into a file named `readinglist.csv` I could do this:

```
./main.py readinglist.csv 'Reading List'
```

#### Import into the Inbox

Example: If I exported my 2Do inbox to `inbox.csv` I could import into the Things Inbox like so:

```
./main.py inbox.csv 'Inbox'
```
