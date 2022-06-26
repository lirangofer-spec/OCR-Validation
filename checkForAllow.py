def checkForAllowed(plate_number: str) -> bool:
    if plate_number[-2:] == '25' or plate_number[-2:] == '26':
        return True
    elif plate_number[-2:] == '87':
        return False
    elif len(plate_number) == 7 and (plate_number[-1:] == '0' or plate_number[-1:] == '5'):
        return False
