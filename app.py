import requests

def trace_ip(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def get_own_ip_info():
    own_ip = requests.get('https://ipinfo.io')
    own_ip_data = own_ip.json()
    return own_ip_data

if __name__ == "__main__":
    while True:
        print("IP Tracer Menu:")
        print("1. Trace a specific IP address")
        print("2. Get information about your own IP")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            ip_address = input("Enter the IP address you want to trace: ")
            traced_data = trace_ip(ip_address)

            if traced_data:
                print("\nIP Tracing Results:")
                print("IP Address: ", traced_data.get("ip"))
                print("Hostname: ", traced_data.get("hostname"))
                print("City: ", traced_data.get("city"))
                print("Region: ", traced_data.get("region"))
                print("Country: ", traced_data.get("country"))
                print("Location: ", traced_data.get("loc"))
                print("Organization: ", traced_data.get("org"))
            else:
                print("Failed to trace IP address.")

        elif choice == "2":
            own_ip_data = get_own_ip_info()
            print("\nYour IP Information:")
            print("IP Address: ", own_ip_data.get("ip"))
            print("Hostname: ", own_ip_data.get("hostname"))
            print("City: ", own_ip_data.get("city"))
            print("Region: ", own_ip_data.get("region"))
            print("Country: ", own_ip_data.get("country"))
            print("Location: ", own_ip_data.get("loc"))
            print("Organization: ", own_ip_data.get("org"))

        elif choice == "3":
            print("Exiting IP Tracer. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
