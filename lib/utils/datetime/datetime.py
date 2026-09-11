def string_to_rtc_datetime(dts):
    tokens = dts.split()
    dta = []
    dta += tokens[0].split("-")
    dta += ["0"]
    dta += tokens[1].split(":")
    dta += ["0"]

    return tuple(map(int, dta))

def string_to_time_datetime(dts):
    tokens = dts.split()
    dta = []
    dta += tokens[0].split("-")
    dta += tokens[1].split(":")
    dta += ["0","0"]

    return tuple(map(int, dta))

def rtc_datetime_to_string(dt:tuple):
    return f"{dt[0]}-{dt[1]:02d}-{dt[2]:02d} {dt[4]:02d}:{dt[5]:02d}:{dt[6]:02d}"

def time_datetime_to_string(dt:tuple):
    return f"{dt[0]}-{dt[1]:02d}-{dt[2]:02d} {dt[3]:02d}:{dt[4]:02d}:{dt[5]:02d}"