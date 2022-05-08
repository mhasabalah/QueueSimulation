from helper import *


interval_time = [0, 2, 4, 4, 2, 2]
service_time = [5, 3, 3, 5, 6, 3]
arrival_time = []
s = 0
able_flage = 1
baker_flage = 1
waiting_flage = 0
able_ser = 0
able_ser_estimated = 0
baker_ser = 0
baker_ser_estimated = 0
systime = 0
waiting = 0
clk = 0
customerqueue = []

for x in range(len(interval_time)):
    s = s + interval_time[x]
    arrival_time.append(s)

def simtime():
    global able_flage
    global baker_flage
    global able_ser
    global able_ser_estimated
    global baker_ser
    global baker_ser_estimated
    global systime
    global waiting
    global arrival_time
    global customerqueue
    global clk
    global waiting_flage
    for x in range(len(interval_time)):
        if able_flage == 1:
            able_flage = 0
            able_ser_estimated = arrival_time[x] + service_time[x]
            able_ser = able_ser + service_time[x]
            if waiting > waiting_flage:
                waiting_flage = waiting
                index = len(customerqueue)-1
                systime = customerqueue[index] + systime + service_time[x]
            else:
                systime = systime + service_time[x]
        elif baker_flage == 1 and able_flage == 0:
            baker_flage = 0
            baker_ser_estimated = arrival_time[x] + service_time[x]
            baker_ser = baker_ser + service_time[x]
            if waiting > waiting_flage:
                waiting_flage = waiting
                index = len(customerqueue) - 1
                systime = customerqueue[index] + systime + service_time[x]
            else:
                systime = systime + service_time[x]
        if x == 5:
            if able_ser_estimated > baker_ser_estimated:
                clk = able_ser_estimated
            else:
                clk = baker_ser_estimated
            break
        if arrival_time[x + 1] >= able_ser_estimated:
            able_flage = 1
        if arrival_time[x + 1] >= baker_ser_estimated:
            baker_flage = 1
        if (arrival_time[x + 1] < able_ser_estimated and arrival_time[x + 1] < baker_ser_estimated):
            if able_ser_estimated - arrival_time[x + 1] > baker_ser_estimated - arrival_time[x + 1]:
                w = baker_ser_estimated - arrival_time[x + 1]
                baker_flage = 1
                arrival_time[x+1] = arrival_time[x+1] + w
                customerqueue.append(w)
                waiting = waiting + w
            else:
                w = able_ser_estimated - arrival_time[x + 1]
                able_flage = 1
                arrival_time[x + 1] = arrival_time[x + 1] + w
                customerqueue.append(w)
                waiting = waiting + w


if __name__ == "__main__":

    total_busy_time_sys = (able_ser+baker_ser) / 2
    simtime()

    avg_waiting_queue(waiting, customerqueue)
    avrage_num_queue(waiting, clk)
    total_busy("Able", able_ser)
    total_busy("Baker", baker_ser)
    total_busy_sys(total_busy_time_sys)
    utlilization(able_ser, clk, "Able")
    utlilization(baker_ser, clk, "Baker")
    utilization_system(total_busy_time_sys, clk)
    avg_serveres_time(able_ser, baker_ser, interval_time)
    avg_waiting_time(waiting, interval_time)
    avg_time_spend_in_sys(systime, interval_time)
    throughput_sys(interval_time, clk)
