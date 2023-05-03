import sys
import requests
from tqdm import tqdm
import validators
from colorama import init, Fore, Back
import pyfiglet

asscii_banner  = pyfiglet.figlet_format('File-D0wn')
print(asscii_banner)

init(autoreset=True)
GREEN = Fore.GREEN
BACKGROUND = Back.BLACK
RED = Fore.RED  


try:
    url  = sys.argv[1] 
    
    if validators.url(url):
        
        file_name = url.split('/')[-1]
        resplose = requests.get(url,stream=True)
        file_size = int(resplose.headers.get('Content-Length',0))
        prosses_bar =tqdm(resplose.iter_content(chunk_size=1024),desc=f'{BACKGROUND}{GREEN}Downloading {file_name}',total=file_size,unit='B',unit_scale=True,unit_divisor=1024,)
        prosses_bar.colour ='green'
        with open(file_name,'wb') as f:   
            for data  in prosses_bar.iterable:
                f.write(data)
                prosses_bar.update(len(data))         
            
    else:
        print(f"{BACKGROUND}{RED}Invalid url!")
except IndexError: 
    print(f"{RED}url not faund!")
except Exception:
    print(f'{BACKGROUND}{RED}Error!')
    
   


