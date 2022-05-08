from helper import *

interval_time = [0, 2, 4, 4, 2, 2]
service_time = [5, 3, 3, 5, 6, 3]
arrival_time = []
s = 0
able_ser = 0
able_ser_estimated = 0
systime = 0
waiting = 0
clk = 0
waiting_falg = 0
customerqueue = []

for x in range(len(interval_time)):
    s = s + interval_time[x]
    arrival_time.append(s)


def simtime():
    global able_ser
    global able_ser_estimated
    global systime
    global waiting
    global arrival_time
    global customerqueue
    global clk
    global waiting_falg
    for x in range(len(interval_time)):
        able_ser_estimated = arrival_time[x] + service_time[x]
        able_ser = able_ser + service_time[x]
        if waiting > waiting_falg:
            waiting_falg = waiting
            index = len(customerqueue)-1
            systime = customerqueue[index]+systime + service_time[x]
        else:
            systime = systime + service_time[x]
        if x == 5:
            clk = able_ser_estimated
            break
        if (arrival_time[x + 1] < able_ser_estimated):
            w = able_ser_estimated - arrival_time[x + 1]
            arrival_time[x + 1] = arrival_time[x + 1] + w
            customerqueue.append(w)
            waiting = waiting + w


if __name__ == "__main__":

    simtime()
    avg_waiting_queue(waiting, customerqueue)
    avrage_num_queue(waiting, clk)
    total_busy_sys(able_ser)
    utilization_system(able_ser, clk)
    avg_server_time(able_ser, interval_time)
    avg_waiting_time(waiting, interval_time)
    avg_time_spend_in_sys(systime, interval_time)
    throughput_sys(interval_time, clk)
