import datetime

time_format = "%Y-%m-%d %H:%M:%S"

expected_data = {
        'title' : 'HomePage',
        'timestamp' : datetime.datetime.strptime('2010-11-18 18:10:33',
            time_format),
        'last accessed' :  datetime.datetime.strptime('2010-11-19 20:02:28', time_format),
        'times accessed' : 24,
        'tags' : None,
        'metadata' :None, 
        'body' : 
"""# Home Sweet Home

## Computer Notes
[[GIT]]


## Gaming
[[WiiNotes]]
## Projects
[[ZimToTrunkNotesSyncScript]]

## Random
[[DownloadList]]

"""
}
