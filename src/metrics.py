import statistics

def get_min_max_avg(data, key):
    values = [float(dp[key]) for dp in data if key in dp]
    if values:
        return min(values), max(values), statistics.mean(values)
    else:
        return None, None, None
