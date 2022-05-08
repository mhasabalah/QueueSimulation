def avrage_num_queue(waiting, clk):
    time_avrage_number_in_queue = "{:.3f}".format(waiting/clk)
    print("time avrage number in queue = " +
          str(time_avrage_number_in_queue)+" cust")


def avg_waiting_queue(waiting, customerqueue):
    avrage_waiting_time_of_those_who_wait = "{:.3f}".format(
        waiting/len(customerqueue))
    print("avrage waiting time of those who wait in queue = " +
          str(avrage_waiting_time_of_those_who_wait)+" min")


def throughput_sys(interval_time, clk):
    throughput = "{:.3f}".format(len(interval_time)/clk)
    print("throughput = " + str(throughput) + " cust/min")


def avg_time_spend_in_sys(systime, interval_time):
    avrage_time_customer_spend_in_sys = "{:.3f}".format(
        systime/len(interval_time))
    print("avrage time customer spend in system = " +
          str(avrage_time_customer_spend_in_sys) + " min")


def avg_waiting_time(waiting, interval_time):
    avrage_waiting_time = "{:.3f}".format(waiting/len(interval_time))
    print("avrage waiting time = " + str(avrage_waiting_time) + " min")


def utlilization(service, clk, name):
    utilization = "{:.3f}".format(service/clk)
    print(f"utilization {name} = "+str(utilization))


def utilization_system(total_busy_time_sys, clk):
    utilization_sys = "{:.3f}".format(total_busy_time_sys/clk)
    print("utilization system = "+str(utilization_sys))


def total_busy_sys(total_busy_time_sys):
    print("total busy time system = " + str(total_busy_time_sys) + " min")


def total_busy(name, service):
    print(f"total busy time {name} = " + str(service) + " min")


def avg_serveres_time(ser1, ser2, interval_time):
    avrage_serve_time = "{:.3f}".format((ser1+ser2) / len(interval_time))
    print("avrage serve time = " + str(avrage_serve_time) + " min")


def avg_server_time(ser, interval_time):
    avrage_serve_time = "{:.3f}".format((ser) / len(interval_time))
    print("avrage serve time = " + str(avrage_serve_time) + " min")
