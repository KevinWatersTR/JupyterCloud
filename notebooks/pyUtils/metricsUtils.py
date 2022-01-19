import oci
import pytz
import json
#
def get_metric_data(compartment,namespace,query,starttime,endtime,  monitoring_client):
    summarize_metrics_data_response = monitoring_client.summarize_metrics_data(
        compartment_id=compartment,
        summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
            namespace=namespace,
            query=query,
            start_time=starttime.astimezone(pytz.timezone('UTC')),
            end_time=endtime.astimezone(pytz.timezone('UTC'))
        ),
        compartment_id_in_subtree=False)
    return summarize_metrics_data_response.data

def print_fn_metrics_data(metricsData,myTimezone):
    for metrics in metricsData:
        for datapoints in metrics.aggregated_datapoints:
            if datapoints.value > 0:
                timestamp = datapoints.timestamp.astimezone(pytz.timezone(myTimezone))
                print ('           '+  timestamp.strftime("%m/%d/%Y %I:%M %p %Z") + '  value: ' \
                    + str(datapoints.value))

def print_apiGtw_metrics_data(metricsData,deployment,myTimezone):
    for metrics in metricsData:
        try:
            if deployment in metrics.dimensions['deploymentName']:

                for datapoints in metrics.aggregated_datapoints:
                    timestamp = datapoints.timestamp.astimezone(pytz.timezone(myTimezone))
                    if datapoints.value > 0:
                        print (timestamp.strftime("%m/%d/%Y %I:%M %p %Z") + '  value: ' + str(datapoints.value))
        except:
            continue
def print_apiGtw_metrics_data_table(metricsData,deployment,myTimezone):
    beginMatrix = "\\begin{array}{|c|c|} \hline"
    matrixHeader =" {\\small  \\textbf{Timestamp} }  & {\\small  \\textbf{Qty}} \\\[2pt]"
    newMatrix =  beginMatrix + " \hline "  + matrixHeader
    endMatrix = "  \end{array} "
    datapointsCnt = 0
    for metrics in metricsData:
        try:
            if deployment in metrics.dimensions['deploymentName']:

                for datapoints in metrics.aggregated_datapoints:
                    timestamp = datapoints.timestamp.astimezone(pytz.timezone(myTimezone))
                    if datapoints.value > 0:
                        datapointsCnt += 1
                        timestamp = datapoints.timestamp.astimezone(pytz.timezone(myTimezone))
                        dtTime = timestamp.strftime("%m/%d/%Y %I:%M %p %Z")
                        matrixRow = "{\\scriptsize \\textsf{"+ dtTime + "}} " + \
                                    "& {\\scriptsize \\textsf{" + str(datapoints.value) + "}} \\\[1pt] "
                        newMatrix = newMatrix + matrixRow
                        # print (timestamp.strftime("%m/%d/%Y %I:%M %p %Z") + '  value: ' + str(datapoints.value))
        except:
            continue
    if datapointsCnt == 0:
        newMatrix = newMatrix + " {\\scriptsize \\textsf{ No Data}} & {\\tiny -} \\\[1pt] "
    return newMatrix + " \hline "  + endMatrix


def get_metrics_list(compartmentId,namespace,monitoring_client):
    metricList = []
    list_metrics_response = monitoring_client.list_metrics(
        compartment_id=compartmentId,
        list_metrics_details=oci.monitoring.models.ListMetricsDetails(namespace=namespace),
        compartment_id_in_subtree=False)
    for metric in list_metrics_response.data:
        metricList.append(metric.name)
    newList = []
    [newList.append(x) for x in metricList if x not in newList]
    return newList

def get_namespace_list(compartmentId,monitoring_client):
    namespaceList =[]
    list_metrics_response = monitoring_client.list_metrics(
        compartment_id=compartmentId,
        list_metrics_details=oci.monitoring.models.ListMetricsDetails(),
        compartment_id_in_subtree=False)
    for metric in list_metrics_response.data:
        namespaceList.append(metric.namespace)
    newList = []
    [newList.append(x) for x in namespaceList if x not in newList]
    return newList    
 
def get_single_metric_record(compartmentId,namespace,metric,monitoring_client):
    list_metrics_response = monitoring_client.list_metrics(
        compartment_id=compartmentId,
        list_metrics_details=oci.monitoring.models.ListMetricsDetails(
        namespace=namespace,
        name=metric),
        compartment_id_in_subtree=False)
    for metric in list_metrics_response.data:
        break
    return metric
def print_fn_metrics_data_table(metricsData,myTimezone):
    beginMatrix = "\\begin{array}{|c|c|} \hline"
    matrixHeader =" \\overset{\\large{\\textbf{Timestamp}}} {\\tiny \\textbf{(" + \
        myTimezone+ " Time Zone)}} "   + \
        " & {\\small  \\textbf{Qty}} \\\[2pt]"
    newMatrix =  beginMatrix + " \hline "  + matrixHeader
    endMatrix = "  \end{array} "
    datapointsCnt = 0
    qtySum =0.0
    for metrics in metricsData:
        for datapoints in metrics.aggregated_datapoints:
            if datapoints.value > 0:
                datapointsCnt += 1
                
                timestamp = datapoints.timestamp.astimezone(pytz.timezone(myTimezone))
                dtTime = timestamp.strftime("%m/%d/%Y %I:%M %p")
                matrixRow = "{\\scriptsize \\textsf{"+ dtTime + "}} " + \
                            "& {\\scriptsize \\textsf{" + str(datapoints.value) + "}} \\\[1pt] "
                newMatrix = newMatrix + matrixRow
                qtySum = qtySum +  datapoints.value
    if datapointsCnt == 0:
        newMatrix = newMatrix + " {\\scriptsize \\textsf{ No Data}} & {\\tiny -} \\\[1pt] "
        return newMatrix + " \hline " + endMatrix
    else:
        totalRow = " {\\small \\textsf{ Total}} & {\\small "+str(qtySum)   +"} \\\[1pt] "
        return newMatrix + " \hline "  + totalRow + " \hline " + endMatrix
def get_speedometer_resource_map(resourceMapFile):
    with open(resourceMapFile) as f:
        data = f.read()
    resourceMap = json.loads(data)
    return resourceMap
