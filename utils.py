import os
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as BS

from config import BUFFER_DIR


def format_date_to_str(number, nb_digit):
    str_nb = str(number)
    if len(str_nb) == nb_digit or len(str_nb) > nb_digit:
        return str_nb
    elif len(str_nb) < nb_digit:
        return '0'+format_date_to_str(number, nb_digit-1)


def format_states_dt(timestamp):
    return f"D{format_date_to_str(timestamp.year, 4)}{format_date_to_str(timestamp.month, 2)}" \
           f"{format_date_to_str(timestamp.day,2)}" \
           f"T{format_date_to_str(timestamp.hour, 2)}{format_date_to_str(timestamp.minute, 2)}" \
           f"{format_date_to_str(timestamp.second, 2)}"


def base10_to_base2_str(num):
    if num % 2 != 0:
        return 0
    div = num // 2
    r = num % 2
    num_base2 = str(r)
    while div != 1 and div != 0:
        num_base2 = str(r) + num_base2
        div = div // 2
        r = div % 2
    res = str(div) + num_base2
    if len(res) < 8:
        while len(res) != 8:
            res = '0' + res 
    return res


def get_network_list(type_connection, network_list, network_list_values,
                     server_hostname=None, server_port=None, folder_file=None):

    if type_connection == 'server':
        if server_hostname is not None and server_port is not None:
            stations_xml = server_hostname + '.' + str(server_port) + '.xml'
        else:
            print('Server hostname/port not defined.')
            return None
    elif type_connection == 'folder':
        if folder_file is not None:
            stations_xml = folder_file
        else:
            print('Folder file not defined')
            return None
    else:
        print('type_connection not defined')
        return None
    try:
        with open(f'config/{type_connection}/{stations_xml}', 'r') as fp:
            content = fp.read()
            config = BS(content, 'lxml-xml')

        for bs_network in config.find_all('Network'):
            network = bs_network.get('code')

            for bs_station in bs_network.find_all('Station'):
                station = bs_station.get('code')

                for bs_channel in bs_station.find_all('Channel'):
                    full_name = network + '.' + station + '.' + \
                                bs_channel.get('locationCode') + '.' + bs_channel.get('code')
                    print(full_name)
                    network_list_values.append(full_name)
                    network_list.append({'label': full_name, 'value': full_name})

        return 1

    except FileNotFoundError:
        print('Config file missing.')
        return -1
    except IndexError:
        print('Verify the config file, no station found')
        return -2


def delete_residual_data(delete_streams=True):
    try:
        for file in os.listdir(BUFFER_DIR):
            if os.path.isdir(BUFFER_DIR+'/'+file) or file == 'streams.data':
                pass
            else:
                os.remove(BUFFER_DIR+'/'+file)
        os.remove(BUFFER_DIR + '/streams.data')
    except PermissionError:
        pass
    except FileNotFoundError:
        try:
            os.mkdir(BUFFER_DIR)
        except FileExistsError:
            pass


if __name__ == '__main__':
    network_list_values = []
    get_network_list('folder', [], network_list_values, folder_file='stations.xml')
    print(network_list_values)
