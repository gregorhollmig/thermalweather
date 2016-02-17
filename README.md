# Thermal Weather

Python3 script that creates a weather status and forecast which can be printed on a simple receipt printer.
I tested it on the "Celectronic D10".
Usage to show in shell:
```shell
python3 weather.py Germany/Karlsruhe

----------------------
   Wetterbericht für
       Karlsruhe
            
     Wolkig bei 2°C
    Gefühlt wie 0°C
                  
          .--.    
       .-(    ).  
      (___.__)__) 
                  
            
         Wind:
       SSW 6km/h
            
 ----------------------
        Vorschau
        Do, 18.2
      Teils Wolkig
    bei 1°C bis 9°C

        Fr, 19.2
     Regen möglich
    bei 2°C bis 7°C

        Sa, 20.2
     Regen möglich
    bei 7°C bis 8°C


```


## Setup 
You have to get an API key from wunderground.com, which is actually free (with certain restrictions).
In the script you can adjust your place to something that suits you more.
