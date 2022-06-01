    1   P = '\x1b[1;97m'
    2   import os,requests
    3   xr = requests.get("http://ip-api.com/json/").json()
    4   try:
    5     	fc = xr["country"]
    6   except KeyError:
    7           print('%s\nBAD INTERNET CONNECTION\n'%(M))
    8           exit()
    9
    10  if __name__ == "__main__":
    11  	os.system("git pull")
    12	        if "Nigeria" == fc:
    13		        __import__("ASTRO").lisensi()
    14	        else:
    15		        __import__("ASTRO").lisensi(
