import keyboard as kb 
from time import sleep as time_sleep 
import json as js

def _2sap_shop():
    with open ("2sap.json", "r") as f :
        db = js.load(f)


    while True:
        print("what drank size would you like to have ")
        print("press, 1 for large, 2 for medium, 3 for small")
        key = kb.read_key()
        time_sleep(0.5)
        if key == '1' :
            print("Done , Enjoy our drink ^_^")
            db["large"]  +=1
            db["total"]  +=15
        elif key == '1' :
            print("Done , Enjoy our drink ^_^")
            db["medium"]  +=1
            db["total"]  +=10
        elif key == '1' : 
            print("Done , Enjoy our drink ^_^")
            db["small"]  +=1
            db["total"]  +=5   
        elif key == 'esc':
            with open ("2sap.json" , 'w') as f:
                js.dump(db , f)
            return    
_2sap_shop()        
    

                                        
                
     
        