> Commit: Chat system
>
> - Created a chat class which creates and holds messages
> - Created a message class which hold information about a message
> - Fixed an incorrect reference to files in the database connection class
> - Sessions now have a chat which they control to also connect chat to the database
> - Chat messages are also now pushed and pulled from/to the database

> Commit: Data management unification
>
> - A session now has a database manager if it is set as remote when created
> - The file manager is now interacted with through the session functions which also run database functions if available
> - Graph generation now uses a try statement to catch any issues with data compilation
> - Renamed the files variable in session to \_files to avoid accidental usage since it should only be used through the session

> Commit: Database connection
>
> - Moved remote mode files into main folder
> - Created a database connection class to push and pull the locally stored session data to the mongo database
> - Created a session class which holds information and data from a session
> - Created a config file to store database configuration settings

> Commit: Generating Graphs
>
> - Created functions to generate line, pie and bar graphs
> - Updated file manager importer function to get csv data
> - Data complier now returns data as a key value pair of chart name and chart data for easier generation

> Commit: File manager
>
> - Moved remote mode specific files to their own folder for now to keep the working path clean.
> - Created file manager class and its functions to add, remove or rename a dataset, add/remove a file and compile a dataset.

> Commit: Project environment setup
>
> - Created a requirements.txt file with all necesary packages.
> - Creates some starting classes for the application
