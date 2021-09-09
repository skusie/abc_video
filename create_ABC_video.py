import os
import subprocess

# video addresses
addresses = """https://www.wdrmaus.de/elefantenseite/#lan_0114_buchstabe_a
https://www.wdrmaus.de/elefantenseite/#lan_0115_buchstabe_b
https://www.wdrmaus.de/elefantenseite/#lan_0116_buchstabe_e
https://www.wdrmaus.de/elefantenseite/#lan_0117_buchstabe_k
https://www.wdrmaus.de/elefantenseite/#lan_0207_buchstabe_t
https://www.wdrmaus.de/elefantenseite/#lan_0208_buchstabe_r
https://www.wdrmaus.de/elefantenseite/#lan_0227_buchstabe_g
https://www.wdrmaus.de/elefantenseite/#lan_0228_buchstabe_l
https://www.wdrmaus.de/elefantenseite/#lan_0254_buchstabe_c
https://www.wdrmaus.de/elefantenseite/#lan_0255_buchstabe_d
https://www.wdrmaus.de/elefantenseite/#lan_0256_buchstabe_f
https://www.wdrmaus.de/elefantenseite/#lan_0298_buchstabe_h
https://www.wdrmaus.de/elefantenseite/#lan_0299_buchstabe_i
https://www.wdrmaus.de/elefantenseite/#lan_0308_buchstabe_j
https://www.wdrmaus.de/elefantenseite/#lan_0320_buchstabe_m
https://www.wdrmaus.de/elefantenseite/#lan_0321_buchstabe_n
https://www.wdrmaus.de/elefantenseite/#lan_0356_buchstabe_p
https://www.wdrmaus.de/elefantenseite/#lan_0357_buchstabe_u
https://www.wdrmaus.de/elefantenseite/#lan_0360_buchstabe_s
https://www.wdrmaus.de/elefantenseite/#lan_0365_buchstabe_o
https://www.wdrmaus.de/elefantenseite/#lan_0366_buchstabe_w
https://www.wdrmaus.de/elefantenseite/#lan_0389_buchstabe_z
https://www.wdrmaus.de/elefantenseite/#lan_0417_buchstabe_q
https://www.wdrmaus.de/elefantenseite/#lan_0421_buchstabe_x
https://www.wdrmaus.de/elefantenseite/#lan_0422_buchstabe_y
https://www.wdrmaus.de/elefantenseite/#lan_0439_buchstabe_v"""

# filenames of downloaded videos
filenames = """LAN 114 Buchstabenmorph A-mdb-2137937.mp4
LAN 115 Buchstabenmorph B-mdb-2137940.mp4
LAN  116 Buchstabenmorph E-mdb-2137957.mp4
LAN   117 Buchstabenmorph K-mdb-2138099.mp4
LAN  207 Buchstabenmorph T -mdb-2138205.mp4
LAN  208 Buchstabenmorph R-mdb-2138171.mp4
LAN  227 Buchstabenmorph G-mdb-2137967.mp4
LAN  228 Buchstabenmorph L -mdb-2138119.mp4
LAN 254 Buchstabenmorph C-mdb-2137935.mp4
LAN 255 Buchstabenmorph D-mdb-2137953.mp4
LAN  256 Buchstabenmorph F-mdb-2137965.mp4
LAN  298 Buchstabenmorph H -mdb-2137971.mp4
LAN  299 Buchstabenmorph  I -mdb-2137976.mp4
LAN  308 Buchstabenmorph  J -mdb-2138096.mp4
LAN 320 Buchstabenmorph M-mdb-2138133.mp4
LAN  321 Buchstabenmorph N-mdb-2138145.mp4
LAN  356 Buchstabenmorph P-mdb-2141723.mp4
LAN  357 Buchstabenmorph U -mdb-2138209.mp4
LAN  360 Buchstabenmorph S -mdb-2138183.mp4
LAN 365 Buchstabenmorph O-mdb-2138151.mp4
LAN  366 Buchstabenmorph W -mdb-2138223.mp4
LAN  389 Buchstabenmorph Z -mdb-2138235.mp4
LAN 417 Buchstabenmorph Q-mdb-2138164.mp4
LAN  421 Buchstabenmorph X -mdb-2138226.mp4
LAN 422 Buchstabenmorph Y -mdb-2138230.mp4
LAN 439 Buchstabenmorph V -mdb-2138216.mp4"""

# download videos
for address in addresses.split('\n'):
#	subprocess.call(['youtube-dl', address])
	pass

# rename videos
for item in filenames.split('\n'):
	letter = item.split('-')[0].replace(' ', '')[-1]
	# TODO catch filenotfound error
#	os.rename(item, letter + '.mp4')
	print(item)

# Generate list of letters A to Z
ABC = []
for i in range(65,91):
    ABC.append(chr(i))


# write a file list for ffmpeg
f = open('ffmpeg_input_list.txt', 'w')
for char in ABC:
	f.write('file \'' + char + '.mp4\'\n')
f.close()


# merge videos
subprocess.run(['ffmpeg', '-f', 'concat', '-i', 'ffmpeg_input_list.txt', "ABC.mp4"])
