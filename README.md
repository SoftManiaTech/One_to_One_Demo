## Switch to Splunk user

```bash
sudo su - splunk
```

## Navigate to Splunk Apps directory

```bash
cd /opt/splunk/etc/apps/
```

## Clone this repository

```bash
git clone https://github.com/SoftManiaTech/One_to_One_Demo.git
```

## Restart Splunk

```bash
cd /opt/splunk/bin
./splunk restart
```

## Execute the script to generate the sample data

```bash
cd /opt/splunk/bin
./splunk cmd python /opt/splunk/etc/apps/One_to_One_Demo/bin/itsi_summary_historical_data.py
```

## Queries

### To see the count of eevents indexed so far

```bash
| tstats count where index="itsi_summary" by index
```

### Raw search

```bash
index=itsi_summary TERM(alert_severity=*)
| timechart span=1sec count by alert_severity
```

### Search with TERM

```bash
| tstats prestats=t count where index=itsi_summary TERM(alert_severity=high) by _time span=1sec
| fillnull "high" alert_severity
| tstats prestats=t append=t count where index=itsi_summary TERM(alert_severity=low) by _time span=1sec
| fillnull "low" alert_severity
| tstats prestats=t append=t count where index=itsi_summary TERM(alert_severity=medium) by _time span=1sec
| fillnull "medium" alert_severity
| tstats prestats=t append=t count where index=itsi_summary TERM(alert_severity=normal) by _time span=1sec
| fillnull "normal" alert_severity
| tstats prestats=t append=t count where index=itsi_summary TERM(alert_severity=unknown) by _time span=1sec
| fillnull "unknown" alert_severity
| timechart limit=50 span=1sec count by alert_severity
```

### Search with PREFIX

```bassh
| tstats count where index=itsi_summary TERM(alert_severity=*) by PREFIX(alert_severity=) _time span=1sec
| rename alert_severity= as alert_severity
| xyseries _time alert_severity count
```
