import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = 'WarunkiNauki'
org = 'some-org'
token = 'some-token'
url = 'http://localhost:8086'

influx_client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

write_api = influx_client.write_api(write_options=SYNCHRONOUS)


def write_measurement(**kwargs):
    p = (influxdb_client.Point(kwargs['measurement'])
         .tag('device', kwargs['device_id'])
         .field('temperature', kwargs['temp'])
         .field('humidity', kwargs['hum']))
    write_api.write(bucket=bucket, org=org, record=p)
