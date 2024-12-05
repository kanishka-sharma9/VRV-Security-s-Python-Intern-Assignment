import re
import pandas as pd
#regex for extracting information out of the logs
log_pattern = r'(?P<Ip_Address>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>.*?)\] "(?P<method>[A-Z]+) (?P<Endpoint>\S+) HTTP/\d\.\d" (?P<status>\d+) (?P<size>\d+)(?: "(?P<error>.*)")?'

def parse_log_line(line):
    try:
        match = re.match(log_pattern, line)
        if match:
            return match.groupdict()
        return None
    except Exception as e:
        raise e
def main():    
    data=[]

    with open("sample.log", "r") as log_file:
        for line in log_file:
            parsed_data = parse_log_line(line)
            if parsed_data:
                # print(parsed_data)
                data.append(parsed_data)


    df=pd.DataFrame(data)

    df.to_csv("Data/log_analysis_results.csv",index=False)

if __name__=="__main__":
    main()