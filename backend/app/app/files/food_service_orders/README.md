Directory	(Function)
----------------------
Error - If a CSV or XML file contains errors, the file collector will stop processing it and place the file in this folder.)
Incoming	-   Files that are to be processed by the file collector are placed here.)
Processed 	-   Files that have been successfully imported by the file collector are placed here.)
Working	-   Files are placed in this folder while the file collector is importing their contents.)


To import a file, place it in the Incoming folder. At the beginning of the next cycle (one of the parameters entered by the user through the Historian Administrator), the system initiates the file import operation, processes the data, stores the result in an archive, and moves the file from the Incoming folder to the Processed folder. During the processing operation, the file moves to the Working folder and the filename changes to YMDHMS-Data.csv or .xml file (for example, 010810103246-data.csv).

When processing is complete, the name changes back to YMDHMS-filename.csv or YMDHMS-file- name.xml, as appropriate (for example, 010810103246-tagtest3line.csv). If errors occur during processing, error messages are logged in the Filecollector_YMDHMS.log file (for example, FileCollector_01081214759.- log) within the LogFiles directory and the file moves to the Error directory.

When the number of days you specify in the Processed File Purge parameter have passed, the system deletes the imported file from the Processed folder. The Error directory is never cleared.
