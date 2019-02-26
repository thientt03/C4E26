from random import *
from check import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text = choice(["blue", "red", "green", "yellow"])
    color = choice(['#3F51B5', '#C62828', '#FFD600', '#4CAF50'])

    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
        if quiz_type == 0:
           
            if text == "blue":  
                n = shapes[0]["rect"]
                is_inside([x,y],n)
                
                    
            elif text == "red":
                n = shapes[1]["rect"]
                is_inside([x,y],n)
                
                   
            elif text == "green":
                n = shapes[2]["rect"]
                is_inside([x,y],n)
                
            else:
                n = shapes[3]["rect"]
                is_inside([x,y],n)
                
                    
            
        else:
            if color == '#3F51B5':
                n = shapes[0]["rect"]
                is_inside([x,y],n)
            
            elif color == '#C62828':
                n = shapes[1]["rect"]
                is_inside([x,y],n)

            elif color == '#FFD600':
                n = shapes[2]["rect"]
                is_inside([x,y],n)
            
            else:
                n = shapes[3]["rect"]
                is_inside([x,y],n)
        return(n)
