# VARIABLES TO CHANGE FOR STATION, COUNTRIES, ...
# SERVER
import pandas as pd

VERBOSE: int = 0

SERVER_DASH_IP: str = "localhost"
SERVER_DASH_PORT: int = 8050
SERVER_DASH_PROTOCOL: str = "http://"
DEBUG: bool = True

# AREA AND STATIONS
NAME_AREA: str = "UB (France)"
LAT_MAP: int = 48
LON_MAP: int = 107
ZOOM_MAP: float = 7

LIST_NAME_STA: list = ['SEMM', 'ARTM', 'UGDM', 'ALFM']
LIST_LAT_STA: list = ['47.561488', '47.926953', '47.638031', '48.00351']
LIST_LON_STA: list = ['106.977964', '107.270435', '107.400533', '106.771986']


# GRAFANA LINK
GRAFANA_DOMAIN: str = "https://monalisa.jeremec.fr/"
GRAFANA_DASHBOARD: str = 'd/pX7YlZH7k/ping-and-cpu?orgId=1'
GRAFANA_REFRESH: str = '10s'
GRAFANA_T_FROM: str = 'now-6h'
GRAFANA_T_TO: str = 'now'

GRAFANA_LINK: str = GRAFANA_DOMAIN + GRAFANA_DASHBOARD + '&refresh=' + \
               GRAFANA_REFRESH + '&from=' + GRAFANA_T_FROM + '&to=' + GRAFANA_T_TO

# UPDATE VAR
UPDATE_TIME_GRAPH: int = 15000  # in ms
UPDATE_DATA: int = 30000
UPDATE_TIME_STATES: int = 100000  # in ms
UPDATE_TIME_ALARMS: int = 60000  # in ms

# STYLE
COLOR_TIME_GRAPH: str = "#ffe476"
TIME_DELTA: pd.Timedelta = pd.Timedelta(60, unit='sec')
HEIGHT_GRAPH: int = 250
TOP_GRAPH: int = 30
BOTTOM_GRAPH: int = 10
LEFT_GRAPH: int = 10
RIGHT_GRAPH: int = 10

# DATA BUFFER
BUFFER_DIR: str = 'data'

# ORACLE CLIENT
CLIENT_ORACLE: str = r'/u01/app/oracle/product/19.3.0/dbhome_1/lib'

# ORACLE CLIENT
HOST_ORACLE: str = '192.168.1.76'
PORT_ORACLE: str = '1522'
SERVICE_ORACLE: str = 'hatdb2'
USER_ORACLE: str = r'hat'
PWD_ORACLE: str = 'mndc_iag'

# for TABLE_ORACLE_XAT and TABLE_ORACLE_SOH, you have to be careful about the class OracleClient in the method
# verify_states if the names are still matching with your database columns
TABLE_ORACLE_XAT: str = 'hatv4'
TABLE_ORACLE_SOH: list = ['DISKSIZE1', 'MASS_POSITION', 'BATTERYVOLTAGE']

# ALARM XAT
XAT_ALARM_NAME: list = ['Loop', 'Water', 'Door 1', 'Door 2']
XAT_NORMAL_STATE: dict = {
    'UB4M': '1100',
    'TEST': '1000',
    'CCBM': '1000',
}

# # SOH ORACLE CLIENT: the two databases are now on the same OracleClient, deprecated
# HOST_ORACLE_SOH: str = '192.168.1.78'
# PORT_ORACLE_SOH: str = '1521'
# SERVICE_ORACLE_SOH: str = 'xe'
# USER_ORACLE_SOH: str = r'sohdata'
# PWD_ORACLE_SOH: str = 'tdb'
# TABLE_ORACLE_SOH: list = ['DISKSIZE1', 'MASS_POSITION', 'BATTERYVOLTAGE']

# SEISMIC CONFIG
XML_INVENTORY: str = ""

# DATA PROCESSING
SAMPLING_RATE: float = 25.0
QUEUE_DURATION: int = 180
