def ips_between(start, end):
    print(start,end)
    startdic ={}
    enddic ={}
    startdic["first"] = int(start.split(".")[0]) 
    startdic["second"] = int(start.split(".")[1])
    startdic["third"] = int(start.split(".")[2]) 
    startdic["fourth"] = int(start.split(".")[3]) 

    enddic["first"] = int(end.split(".")[0]) 
    enddic["second"] = int(end.split(".")[1]) 
    enddic["third"] = int(end.split(".")[2]) 
    enddic["fourth"] = int(end.split(".")[3]) 

    start_total = startdic["first"]*256**3+startdic["second"]*256**2+startdic["third"]*256+startdic["fourth"]
    end_total = enddic["first"]*256**3+enddic["second"]*256**2+enddic["third"]*256+enddic["fourth"]

    sum = end_total-start_total
    print(sum)
    return sum





ips_between ("20.0.0.250", "20.0.1.0")