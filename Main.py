import numpy as np
import json
import datetime
import random
import string
from Data import alerts, service_names, regions, severity_levels, environments, relevant_tags_prom, relevant_tags_home


def load_json(f_name):
    # Opening JSON file
    f = open(f_name)

    # returns JSON object as a dictionary
    data = json.load(f)

    # Closing file
    f.close()

    return data


def gen_alert_date_time(start_monitoring_dt, end_monitoring_dt, max_alert_time_minutes=10):
    t1 = start_monitoring_dt.timestamp()
    t2 = end_monitoring_dt.timestamp()

    # Get a random start time between t1 and (t2 - max_separation)
    max_separation_seconds = max_alert_time_minutes * 60
    start_time = random.uniform(t1, t2 - max_separation_seconds)

    # Generate the second time by adding a random number of seconds up to max_separation
    end_time = start_time + random.uniform(0, max_separation_seconds)

    # Convert the timestamps back to datetime objects
    dt1 = datetime.datetime.fromtimestamp(start_time)
    dt2 = datetime.datetime.fromtimestamp(end_time)

    dt1_iso = dt1.strftime('%Y-%m-%dT%H:%M:%SZ')
    dt2_iso = dt2.strftime('%Y-%m-%dT%H:%M:%SZ')

    return dt1_iso, dt2_iso


def gen_ip_with_port():
    ip = ".".join(str(random.randint(1, 255)) for i in range(4))
    port = random.randint(1024, 65535)
    return f"{ip}:{port}"


def gen_fingerprint(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))


def gen_name_msg(names_list=service_names, alerts_dict=alerts):
    rndm_service = random.choice(names_list)
    alert_names = list(alerts_dict.keys())
    rndm_alert = random.choice(alert_names)
    alert_msg = alerts_dict[rndm_alert]
    return rndm_service + rndm_alert, alert_msg


def generate_prom_alerts(all_tags, instances, fingerprints, rel_prom_tags=relevant_tags_prom, severity_lvls=severity_levels, reg=regions, env=environments):
    prom_alert_dict = {}
    name, msg = gen_name_msg()
    sev = random.choice(severity_lvls)
    envr = random.choice(env)
    regn = random.choice(reg)
    inst = random.choice(instances)
    fing = random.choice(fingerprints)
    d1 = datetime.datetime(2024, 7, 12, 8, 0, 0)
    d2 = datetime.datetime(2024, 7, 12, 10, 0, 0)
    t1, t2 = gen_alert_date_time(d1, d2)

    for tag in all_tags:
        if tag in rel_prom_tags:
            if tag == 'name':
                prom_alert_dict[tag] = name
            if tag == 'env':
                prom_alert_dict[tag] = envr
            if tag == 'severity':
                prom_alert_dict[tag] = sev
            if tag == 'description':
                prom_alert_dict[tag] = msg
            if tag == 'region':
                prom_alert_dict[tag] = regn
            if tag == 'instance':
                prom_alert_dict[tag] = inst
            if tag == 'startsAt':
                prom_alert_dict[tag] = t1
            if tag == 'endsAt':
                prom_alert_dict[tag] = t2
            if tag == 'fingerprint':
                prom_alert_dict[tag] = fing
        else:
            prom_alert_dict[tag] = gen_fingerprint(20)

    return prom_alert_dict


def generate_home_alerts(all_tags, rel_home_tags=relevant_tags_home, severity_lvls=severity_levels):
    home_alert_dict = {}
    name, msg = gen_name_msg()
    sev = random.choice(severity_lvls)
    for tag in all_tags:
        if tag in rel_home_tags:
            if tag == 'name':
                home_alert_dict[tag] = name
            if tag == 'severity':
                home_alert_dict[tag] = sev
            if tag == 'message':
                home_alert_dict[tag] = msg + f', Name: {name}' + f', severity: {sev}'

    return home_alert_dict


if __name__ == '__main__':
    #### Testing ####
    # print("Hello Keep")
    # a = np.zeros(5)
    # print(a)
    #
    # b = load_json('Alert_prom.json')
    # print(b)
    # print(len(b.keys()))
    #
    # c = load_json('Alert_home.json')
    # print(c.keys())
    #
    # # Given datetimes
    # d1 = datetime.datetime(2024, 7, 12, 8, 0, 0)
    # d2 = datetime.datetime(2024, 7, 12, 10, 0, 0)
    #
    # # Generate and print the two datetimes
    # dt1, dt2 = gen_alert_date_time(d1, d2)
    # print("Datetime 1:", dt1)
    # print("Datetime 2:", dt2)
    #
    # # Generate an IP address and port
    # ip_with_port = gen_ip_with_port()
    #
    # # Print the IP address and port
    # print(ip_with_port)
    #
    # # Print fingerprint
    # print(gen_fingerprint())
    #
    # print(gen_name_msg(service_names, alerts))
    #
    # print(generate_home_alerts(list(c.keys())))

    # print(generate_prom_alerts(list(b.keys()), instances_list, fingerprints_list))

    #### Main Run ####

    b = load_json('Alert_prom.json')
    c = load_json('Alert_home.json')

    instances_list = [gen_ip_with_port() for i in range(50)]
    fingerprints_list = [gen_fingerprint() for i in range(200)]

    for i in range(800):
        filename = f'Generated Alerts/sample{i}.json'
        with open(filename, 'w') as file:
            json.dump(generate_prom_alerts(list(b.keys()), instances_list, fingerprints_list), file, indent=2)
    for i in range(200):
        filename = f'Generated Alerts/sample{i+800}.json'
        with open(filename, 'w') as file:
            json.dump(generate_home_alerts(list(c.keys())), file, indent=2)


