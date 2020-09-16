import cocos
import random
import pyglet
from pyglet.window import key
from cocos.scenes import *
from cocos.director import director

class Math_Scene(cocos.scene.Scene):
    def __init__(self):
        super().__init__()
        self.add(BGMathQuick())
        global flag
        flag = 1

        self.add(Question())
        self.add(Answer())


class Answer(cocos.layer.Layer):
    is_event_handler = True

    global kol
    kol = 0

    global pop1
    pop1 = 560
    def __init__(self):
        super(Answer, self).__init__()
        global pop1
        
        self.active = True
        self.text = cocos.text.Label("",
        font_name='Times New Roman',
        font_size=32,
        #x=510, y=645)
        x=515, y=pop1)
        
        
        self.text_answer = cocos.text.Label("23",
        font_name='Times New Roman',
        font_size=32,
        #x=710, y=645)
        x = 715, y = pop1)
        
        
        self.keys_pressed = ""
        self.user_answer = ""
        self.text.element.text = self.keys_pressed
        self.text_answer.element.text = self.user_answer
        
        self.add(self.text)
        self.add(self.text_answer)

    def on_key_press(self, symbol, modifiers):
        global pop1
        if not self.active:
            return
        
        if symbol == key.ENTER:
            if int(self.keys_pressed) != num1 + num2:
                self.user_answer = 'Wrong'

                self.text.element.text = self.keys_pressed
                self.text_answer.element.text = self.user_answer
            else:
                self.user_answer = 'Correct'
                self.text.element.text = self.keys_pressed
                self.text_answer.element.text = self.user_answer
            if (self.user_answer == 'Correct'):
                pop1 -= 40

                self.user_answer = 'Wrong'
                self.add(Question())
                self.add(Answer())
                self.active = False

        else:
            kk = pyglet.window.key.symbol_string(symbol)
            if kk == "SPACE":
                kk = " "
            if kk == "BACKSPACE":
                self.keys_pressed = self.keys_pressed[:-1]
            else:
                ignored_keys = ("LSHIFT", "RSHIFT", "LCTRL", "RCTRL", "LCOMMAND", 
                                "RCOMMAND", "LOPTION", "ROPTION","SPACE",)
                if kk not in ignored_keys and kk.replace('_','').isnumeric():
                    self.keys_pressed = (self.keys_pressed + kk).replace('_','')
            #self.update_text()
            self.text.element.text = self.keys_pressed
            self.text_answer.element.text = self.user_answer
        

class Question(cocos.layer.Layer):
    global pop
    pop= 617
    def __init__(self):
        super(Question, self).__init__()

        global num1
        global num2
        global pop
        
        print(pop)
        pop -= 40

        pos_y = (pop)
        self.question_str = ""
        self.question_label = cocos.text.Label(
        self.question_str,
        font_name='Times New Roman',
        font_size=32,
        anchor_x='center', anchor_y='center'
        )

        pos_x = 430

        self.question_label.position =  pos_x,pos_y
        self.add(self.question_label)

        
        self.question_str = ""
        self.question_label.element.text = self.question_str

        num1 = random.randint(0, 25)
        num2 = random.randint(0, 25)
        
        self.question_str = "{} + {} = ".format(num1, num2)
        
        if num1 < num2:
                num1, num2 = num2, num1

        self.question_label.element.text = self.question_str

class BGMathQuick(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        bg = cocos.sprite.Sprite('Mini_Games/QuickMath/res/bgmathquick.png')
        bg.position = 630, 470
        self.add(bg)

if __name__ == "__main__":

    director.init(width=1260, height= 941, caption="University")
    director.window.pop_handlers()
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    global pop
    pop = 660
    
    question_scene = Question()

    active_scene = Math_Scene()
    
    director.run(active_scene)
