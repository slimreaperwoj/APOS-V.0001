from memory import Memory

class APOSRobot:
    
    def __init__(self, name):
        self.name = name
        self.memory = Memory()

        self.traits = {

            "curiosity": 50,
            "patience": 50, 
            "trust": 50,
            "confidence": 50,
            "sociability": 50,
            "persistence": 50,
            "caution": 50 , 



        }

        self.cognitive_traits = {
            "intelligence": 50,
            "creativity": 50,
            "knowledge": 50,

        }


        self.experiences = {

            "success": {

                "curiosity": 2,
                "confidence":3,
                "persistence": 2,

            },

         
            "failed": {
                "patience": -2,
                "confidence": -3,
                "persistence": 1,
            
        },
         "praised": {
                "sociability": 1,
                "confidence": 2,
                "trust": 1,
            }

            
        }

        
        
        

       

    





    def personality(self):

        if any(value < 0 for value in self.traits.values()):
            print("Personality attributes are below zero. Please check the values.")
            return 

        elif any(value > 100 for value in self.traits.values()):
            print("Personality attributes are above 100. Please check the values.")
            return
        else:
            print("Personality attributes are within the normal range.")
            print("Personality Attributes:")
            for traits, value in self.traits.items():
                print(f"  {traits.capitalize()}: {value}")
           


    def cognitive(self):
        if any(value < 0 for value in self.cognitive_traits.values()):
            print("Cognitive attributes are below zero. Please check the values.")
            return 

        elif any(value > 100 for value in self.cognitive_traits.values()):
            print("Cognitive attributes are above 100. Please check the values.")
            return
        else:
            print("Cognitive attributes are within the normal range.")
            print("Cognitive Attributes:")
            for cognitive, value in self.cognitive_traits.items():
                print(f"  {cognitive.capitalize()}: {value}")

        
    def change_trust(self, amount):
        old_trust = self.traits["trust"]

        self.traits["trust"] += amount
        self.traits["trust"] = min(self.traits["trust"], 100)
        self.traits["trust"] = max(self.traits["trust"], 0)

        actual_change = self.traits["trust"] - old_trust

        if actual_change > 0:
            print("Trust increased by", actual_change)

        elif actual_change < 0:
            print("Trust decreased by", -actual_change)

        else:
            print("Trust did not change.")

        


    def experience(self, event):

        if event in self.experiences:
        
            for trait, change in self.experiences[event].items():
                print(f"Experience '{event}' occurred. Changing traits accordingly.")
                self.traits[trait] += change
                self.traits[trait] = min(self.traits[trait], 100)
                self.traits[trait] = max(self.traits[trait], 0)

            self.memory.add_memory(event)


        else: 
            print(f"Experience '{event}' not recognized. No changes made to traits.")

            
            
    





        



