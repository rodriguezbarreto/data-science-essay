from sanitizator.sanitizator import sanitizator

origin = 'database/origin'
destiny = 'database/new'


# Receives origin folder and destination folder path.And sanitizes tables.
sanitizator(origin, destiny)
