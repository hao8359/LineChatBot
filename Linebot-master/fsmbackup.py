from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message, send_image_url
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "hotlist"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "recommendation"
	
    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "introduction"
   
    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "hot 1"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "hot 2"

    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "hot 3"

    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "hot 4"

    def is_going_to_state8(self, event):
        text = event.message.text
        return text.lower() == "hot 5"

    def is_going_to_state9(self, event):
        text = event.message.text
        return text.lower() == "hot 6"

    def is_going_to_state10(self, event):
        text = event.message.text
        return text.lower() == "hot 7"

    def is_going_to_state11(self, event):
        text = event.message.text
        return text.lower() == "hot 8"

    def is_going_to_state12(self, event):
        text = event.message.text
        return text.lower() == "hot 9"

    def is_going_to_state13(self, event):
        text = event.message.text
        return text.lower() == "hot 10"
    def is_going_to_state14(self, event):
        text = event.message.text
        return text.lower() == "help"
    def is_going_to_state15(self, event):
        text = event.message.text
        return text.lower() == "fsm"
    def is_going_to_state16(self, event):
        text = event.message.text
        return text.lower() == "add"
    def is_going_to_state17(self, event):
        text = event.message.text
        return text.lower() == "bye bye"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.billboard.com/charts/hot-100")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        music = ['https://www.youtube.com/watch?v=_NGQfFCFUn4', 'https://www.youtube.com/watch?v=GJ63esXbY-M&list=RDGJ63esXbY-M&start_radio=1', 'https://www.youtube.com/watch?v=hxQLe6nlUcA', 'https://www.youtube.com/watch?v=MPbUaIZAaeA', 'https://www.youtube.com/watch?v=pE49WK-oNjU', 'https://www.youtube.com/watch?v=L3_4OXQVNgc']
        reply_token = event.reply_token
        send_text_message(reply_token, music[random.randint(0,5)])
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "本州排行第一的是Taylor Swifty在2020年12月11日發行的全新單曲 willow"+"\n"+"這支單曲收錄於同日發行的最新專輯《evermore》中。《evermore》作為約半年前發行的《folklore》之姊妹專輯但帶有較強烈的秋冬氣息。而willow 與專輯中的其他首歌都是以indie混一些民謠鄉村的風格呈現，這首歌的名字來自抒情詩「生活是一棵柳樹，它隨風而轉」，歌詞更是「Life was willow when they bent right to your wind」呼應，描述了一個女孩在預期之外愛上了一個男孩，即使兩人有許多的差異，卻相互磨合互補，女孩也願意為了愛情奉獻自己與對方相伴")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

    
    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=F3JyzuDIV3I")
        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://youtu.be/gr2DjP6y1-k")
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")

    def on_enter_state6(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://instagram.com/feichi1124?utm_medium=copy_link")
        self.go_back()

    def on_exit_state6(self):
        print("Leaving state6")

    def on_enter_state7(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://youtu.be/eZ9poBAcJUU")
        self.go_back()


    def on_exit_state7(self):
        print("Leaving state7")

    def on_enter_state8(self, event):
        print("I'm entering state8")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=GrAchTdepsU")
        self.go_back()

    def on_exit_state8(self):
        print("Leaving state8")

    def on_enter_state9(self, event):
        print("I'm entering state9")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=brTYTuromPY")
        self.go_back()

    def on_exit_state9(self):
        print("Leaving state9")

    def on_enter_state10(self, event):
        print("I'm entering state10")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=AN_R4pR1hck")
        self.go_back()

    def on_exit_state10(self):
        print("Leaving state10")

    def on_enter_state11(self, event):
        print("I'm entering state11")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=tcYodQoapMg")
        self.go_back()

    def on_exit_state11(self):
        print("Leaving state11")

    def on_enter_state12(self, event):
        print("I'm entering state12")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=gdZLi9oWNZg")
        self.go_back()

    def on_exit_state12(self):
        print("Leaving state12")

    def on_enter_state13(self, event):
        print("I'm entering state13")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://youtu.be/W1VnkIFKiFc")
        self.go_back()

    def on_exit_state13(self):
        print("Leaving state13")

    def on_enter_state14(self, event):
        print("I'm entering state14")
        reply_token = event.reply_token
        send_text_message(reply_token, "https://docs.google.com/presentation/d/1HSf3-m6_h9Uv2N_y9mgOG6fOho-bRhl0oInhHdC45ZU/edit#slide=id.g25a54d5e5a4faf37_26")
        
        self.go_back()

    def on_exit_state14(self):
        print("Leaving state14")

    def on_enter_state15(self, event):
        print("I'm entering state15")
        reply_token = event.reply_token
        send_image_url(reply_token, "https://img.onl/XEYT6V")
        
        self.go_back()

    def on_exit_state15(self):
        print("Leaving state15")

    def on_enter_state16(self, event):
        print("I'm entering state16")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.instagram.com/p/CVeyJ6Ajr43/?utm_source=ig_web_copy_link")
        self.go_back()

    def on_exit_state16(self):
        print("Leaving state16")

    def on_enter_state17(self, event):
        print("I'm entering state17")

        reply_token = event.reply_token
        send_text_message(reply_token, "good bye my boy")
        self.go_back()

    def on_exit_state17(self):
        print("Leaving state17")