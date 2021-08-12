import speedtest

print('**********Finding the best server for your speedtest************')
speed = speedtest.Speedtest()
best_server = speed.get_best_server()
download = speed.download()
upload = speed.upload()
isp = speed.get_config()
ping= speed.results.ping

print(f"Find the best server: {best_server['host']}\t Location:{best_server['name']}\tCountry:{best_server['country']}")
print(f"Your Download speed is:{download /1024 /1024:.2f} Mbit")
print(f"Your Upload speed is: {upload/1024 /1024:.2f} Mbit")
print(f"Your Ping ms : {ping} ms")
print(f"Your Isp ip: {isp['client']['ip']}\tYour Isp name:{isp['client']['isp']}")