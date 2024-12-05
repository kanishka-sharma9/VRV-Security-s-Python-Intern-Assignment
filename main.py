#Required Imports
import pandas as pd
import cli

#Read the DataFrame
df=pd.read_csv('Data/log_analysis_results.csv')

while True:
    cli.main_menu()
    request=int(input("Enter Choice:"))
    #Count Requests per IP Address
    if request==1:
        request_counts = df['Ip_Address'].value_counts().reset_index()
        request_counts.columns = ['Ip Address', 'Request Count']
        request_counts.sort_values(by='Request Count', ascending=False,inplace=True)
        request_counts.to_csv("Results/output1.csv",index=False)
        print("\n\n",request_counts,end="\n\n\n")
    
    #Identify the Most Frequently Accessed Endpoint
    if request==2:
        endpoint_counts = df['Endpoint'].value_counts().reset_index()
        endpoint_counts.columns = ['Endpoint', 'Access Count']
        top_endpoint=endpoint_counts.iloc[0]
        print("\n\nMost Frequently Accessed Endpoint:")
        print(f"{top_endpoint.__getitem__("Endpoint")} (Accessed {top_endpoint.__getitem__("Access Count")} times)",end="\n\n\n")
        endpoint_counts.iloc[0:1,:].to_csv("Results/output2.csv",index=False)

    #Detect Suspicious Activity
    if request==3:
        failed_login_attempts = df[df['error'] == 'Invalid credentials']
        threshold = int(input("Enter Threshold Value:"))
        failed_login_counts = failed_login_attempts['Ip_Address'].value_counts()
        flagged_ips = failed_login_counts[failed_login_counts > threshold]
        
        print("\n\nSuspicious Activity Detected:")
        
        flagged_ips_df = flagged_ips.reset_index()
        flagged_ips_df.columns = ['Ip_Address', 'Failed Login Attempts']
        flagged_ips_df.to_csv("Results/output3.csv",index=False)
        print(flagged_ips_df,end="\n\n\n")
    #exit the program
    if request==4:
        exit(0)