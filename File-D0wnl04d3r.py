import sys
import requests
from tqdm import tqdm
import validators
from colorama import init, Fore, Back
import pyfiglet

asscii_banner  = pyfiglet.figlet_format('File-D0wn')
print(asscii_banner)


#*colorama code
init(autoreset=True)
GREEN = Fore.GREEN
BACKGROUND = Back.BLACK
RED = Fore.RED  


try:
    url  = sys.argv[1] #!get in terminal url
    #?url validation
    if validators.url(url):
        
        file_name = url.split('/')[-1]
        resplose = requests.get(url,stream=True)
        file_size = int(resplose.headers.get('Content-Length',0))
        
        #!We use resp.iter_content to iterate over chunks of data with a fixed chunk_size
        #!To set up the tqdm we use unit, unit_scale and unit_divisor to convert iterations into B, KB, or MB so that it will look more meaningful. Inside the iteration, we write the chunk to the disc and update the tqdm pbar with the length of the chunk.
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
    
   


