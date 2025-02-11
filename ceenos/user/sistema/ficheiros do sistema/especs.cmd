@echo off
wmic cpu get name > cpu.txt
wmic cpu get maxclockspeed > fq.txt
::wmic cpu get numberofcores >> especs.txt
::wmic cpu get numberoflogicalprocessors >> especs.txt
wmic memorychip get capacity > ram.txt
::wmic memorychip get speed >> especs.txt
wmic diskdrive get size > arm.txt
wmic path Win32_VideoController get name > pv.txt
wmic os get osarchitecture > arq.txt
::wmic computersystem get model,name,manufacturer,systemtype >> arq.txt
wmic computersystem get model >> arq.txt
wmic computersystem get manufacturer >> arq.txt
wmic computersystem get systemtype >> arq.txt
