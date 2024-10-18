import random
import time
from datetime import datetime

# Predefined data for events
kpibasesearch = "5dd8512622092b554f3e7da7"
kpi_list = ["Average Alert Severity", "Service Latency", "System Health"]
service_ids = ["9a6bdac6-fa6c-423e-81dc-785dbf75637e", "bc6a8cd9-123f-4b6a-839d-dbc6fef9b6e3"]
alert_colors = ["#F26A35", "#D9534F", "#5CB85C"]
hostname = "https://itsisearch.customer.com:443"

# Function to generate the event
def generate_event():
    current_time = time.time()
    min_time = current_time - 300  # Events 5 minutes old
    max_time = current_time
    
    event = {
        "time": datetime.utcnow().isoformat() + 'Z',  # Current UTC time
        "search_name": f"Indicator - Shared - {kpibasesearch} - ITSI Search",
        "search_now": current_time,
        "info_min_time": min_time,
        "info_max_time": max_time,
        "info_search_time": current_time + random.uniform(1, 5),  # Some delay in search
        "kpi": random.choice(kpi_list),
        "kpiid": "ec77165d-e79f-4379-9534-3479954e64a6",
        "urgency": random.randint(1, 5),  # Random urgency
        "serviceid": random.choice(service_ids),
        "itsi_service_id": random.choice(service_ids),
        "is_service_aggregate": 1,
        "is_entity_in_maintenance": 0,
        "is_entity_defined": 0,
        "entity_key": "service_aggregate",
        "is_service_in_maintenance": 0,
        "kpibasesearch": kpibasesearch,
        "is_filled_gap_event": 0,
        "alert_color": random.choice(alert_colors),
        "alert_level": random.randint(3, 5),  # Alerts are typically at level 3 or above
        "alert_value": random.randint(1, 100),
        "itsi_kpi_id": "ec77165d-e79f-4379-9534-3479954e64a6",
        "is_service_max_severity_event": 1,
        "alert_severity": random.choice(["high", "medium", "low"]),
        "alert_period": random.randint(1, 60),  # In minutes
        "entity_title": "service_aggregate",
        "hostname": hostname
    }
    
    # Format the event in log format
    log_event = (
        f'{datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")} +0000, '
        f'search_name="{event["search_name"]}", '
        f'search_now={event["search_now"]:.3f}, '
        f'info_min_time={event["info_min_time"]:.3f}, '
        f'info_max_time={event["info_max_time"]:.3f}, '
        f'info_search_time={event["info_search_time"]:.3f}, '
        f'kpi="{event["kpi"]}", '
        f'kpiid="{event["kpiid"]}", '
        f'urgency={event["urgency"]}, '
        f'serviceid="{event["serviceid"]}", '
        f'itsi_service_id="{event["itsi_service_id"]}", '
        f'is_service_aggregate={event["is_service_aggregate"]}, '
        f'is_entity_in_maintenance={event["is_entity_in_maintenance"]}, '
        f'is_entity_defined={event["is_entity_defined"]}, '
        f'entity_key={event["entity_key"]}, '  # No quotes for entity_key
        f'is_service_in_maintenance={event["is_service_in_maintenance"]}, '
        f'kpibasesearch={event["kpibasesearch"]}, '  # No quotes for kpibasesearch
        f'is_filled_gap_event={event["is_filled_gap_event"]}, '
        f'alert_color="{event["alert_color"]}", '
        f'alert_level={event["alert_level"]}, '
        f'alert_value={event["alert_value"]}, '
        f'itsi_kpi_id="{event["itsi_kpi_id"]}", '
        f'is_service_max_severity_event={event["is_service_max_severity_event"]}, '
        f'alert_severity={event["alert_severity"]}, '  # No quotes for alert_severity
        f'alert_period={event["alert_period"]}, '  # No quotes for alert_period
        f'entity_title={event["entity_title"]}, '  # No quotes for entity_title
        f'hostname="{event["hostname"]}"'
    )
    
    return log_event

# Function to generate and print 10,000 events
def generate_10000_events():
    for _ in range(10000):
        print(generate_event())
        time.sleep(0.000001)  # Sleep for 1 microsecond between events

# Example of event generation
if __name__ == "__main__":
    generate_10000_events()
