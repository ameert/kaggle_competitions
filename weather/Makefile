# this makefile downloads some basic info and sets everything up

local_path=pwd
www_path=ftp://ftp.ncdc.noaa.gov/pub/data/noaa
mysql_cmd='mysql -u pymorph -ppymorph catalog'

#all: .download

.download:
	wget ${www_path}/ishJava.class -O ./scripts/ishJava.class;\
	wget ${www_path}/ishJava_ReadMe.pdf -O ./documentation/ishJava_ReadMe.pdf;\
	wget ${www_path}/ish-format-document.pdf -O ./documentation/ish-format-document.pdf;\
	wget ${www_path}/readme.txt -O ./documentation/weather_readme.txt;\
	wget ${www_path}/country-list.txt -O ./data/setup/country-list.txt;\
	wget ${www_path}/isd-history.csv -O ./data/setup/isd-history.csv;\
	wget ${www_path}/isd-inventory.csv -O ./data/setup/isd-inventory.csv;

#.setup: .download


#.mysql:

cleanhidden:
	rm -f .data;\
	rm -f .setup;\
	rm -f .mysql;

clean: cleanhidden
	rm ./data/*;\
	rm ./data/setup/*;\
	rm ./documentation/*;\
	rm ./scripts/ishJava.class;\

