wmic cpu get name,caption,deviceid,maxclockspeed,numberofcoores,numeroflogicalprocessors
wmic memorychip get capacity,manufacer,partnumber,speed
wmic diskdrive get caption,size,model,interfacetype
wmic path Win32_VideoController get name,deviceid,driverversion
wmic nic get name,macadress,netconnectionstatus
wmic os get caption,version,os,architecture,installdate
