from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message, send_image_url
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "主場"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "精彩剪輯"
	
    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "介紹"
   
    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "24"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "32"

    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "77"

    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "64"

    def is_going_to_state8(self, event):
        text = event.message.text
        return text.lower() == "68"

    def is_going_to_state9(self, event):
        text = event.message.text
        return text.lower() == "39"

    def is_going_to_state10(self, event):
        text = event.message.text
        return text.lower() == "31"

    def is_going_to_state11(self, event):
        text = event.message.text
        return text.lower() == "5"

    def is_going_to_state12(self, event):
        text = event.message.text
        return text.lower() == "66"

    def is_going_to_state13(self, event):
        text = event.message.text
        return text.lower() == "12"
    def is_going_to_state14(self, event):
        text = event.message.text
        return text.lower() == "幫助"
    def is_going_to_state15(self, event):
        text = event.message.text
        return text.lower() == "fsm"
    def is_going_to_state16(self, event):
        text = event.message.text
        return text.lower() == "歌曲推薦"
    def is_going_to_state17(self, event):
        text = event.message.text
        return text.lower() == "ug"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "台南市立棒球場")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        play = ['https://www.youtube.com/watch?v=iFyheD71V6o', 'https://www.youtube.com/watch?v=r8RONH5c9xQ', 'https://www.youtube.com/watch?v=W-HA3H-rAkU', 'https://www.youtube.com/watch?v=5akZH9FMf7w', 'https://www.youtube.com/watch?v=qYCLA-JLdiw', 'https://www.youtube.com/watch?v=odwYUElukyI','https://www.youtube.com/watch?v=_XTOy1bgCJE','https://www.youtube.com/watch?v=_tr8lIOrXuY','https://www.youtube.com/watch?v=Ou0YKPOdM6M','https://www.youtube.com/watch?v=1flIXnij65w']
        reply_token = event.reply_token
        send_text_message(reply_token, play[random.randint(0,9)])
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "這是介紹台灣元老級球隊[統一獅]的互動式聊天機器人")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

    
    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=zdQuBGxpZyc")
        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=dInzAWptnYU")
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")

    def on_enter_state6(self, event):
        print("I'm entering state6")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://youtu.be/aOmGchxlap0")
        self.go_back()

    def on_exit_state6(self):
        print("Leaving state6")

    def on_enter_state7(self, event):
        print("I'm entering state7")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=NHTsG0PI7yA")
        self.go_back()


    def on_exit_state7(self):
        print("Leaving state7")

    def on_enter_state8(self, event):
        print("I'm entering state8")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=_I3DqlX1LJI")
        self.go_back()

    def on_exit_state8(self):
        print("Leaving state8")

    def on_enter_state9(self, event):
        print("I'm entering state9")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=FpNvId-mqVA")
        self.go_back()

    def on_exit_state9(self):
        print("Leaving state9")

    def on_enter_state10(self, event):
        print("I'm entering state10")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=1xlaSudqSZY")
        self.go_back()

    def on_exit_state10(self):
        print("Leaving state10")

    def on_enter_state11(self, event):
        print("I'm entering state11")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=VTvwE5lSXRc")
        self.go_back()

    def on_exit_state11(self):
        print("Leaving state11")

    def on_enter_state12(self, event):
        print("I'm entering state12")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=VUwiEmBuROA")
        self.go_back()

    def on_exit_state12(self):
        print("Leaving state12")

    def on_enter_state13(self, event):
        print("I'm entering state13")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=Vh_etwp0MOo&t=16s")
        self.go_back()

    def on_exit_state13(self):
        print("Leaving state13")

    def on_enter_state14(self, event):
        print("I'm entering state14")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入以下可行指令 : \n主場 \n精彩剪輯 \n介紹 \n24 \n32 \n77 \n64 \n68 \n39 \n31 \n5 \n66 \n12 \n幫助 \nfsm \n歌曲推薦 \nug")
        
        self.go_back()

    def on_exit_state14(self):
        print("Leaving state14")

    def on_enter_state15(self, event):
        print("I'm entering state15")
        reply_token = event.reply_token
        send_image_url(reply_token, "https://i.imgur.com/NpWbp7B.png")
        
        self.go_back()

    def on_exit_state15(self):
        print("Leaving state15")

    def on_enter_state16(self, event):
        print("I'm entering state16")
        music = ['https://www.youtube.com/watch?v=bfHV4tmAhg4','https://www.youtube.com/watch?v=I4Mes83cCYU&list=RDCMUC1tHuRanhZ8i4fEKSNhhNJQ&index=2','https://www.youtube.com/watch?v=gxzBmvQoE6k&list=RDCMUC1tHuRanhZ8i4fEKSNhhNJQ&index=4','https://www.youtube.com/watch?v=AeLWAkbGUhc','https://www.youtube.com/watch?v=UjXLH5byv7U','https://www.youtube.com/watch?v=QzHVkSBylPQ','https://www.youtube.com/watch?v=5UQv4oQttA0','https://www.youtube.com/watch?v=6c2O6qVabhk']
        reply_token = event.reply_token
        send_text_message(reply_token, music[random.randint(0,7)])
        self.go_back()

    def on_exit_state16(self):
        print("Leaving state16")

    def on_enter_state17(self, event):
        print("I'm entering state17 ")
        members = ['https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/p180x540/241233801_890682854867933_324571164724022520_n.jpg?_nc_cat=101&_nc_rgb565=1&ccb=1-5&_nc_sid=825194&_nc_ohc=DnmELfGi6VwAX-KcP0A&_nc_ht=scontent-tpe1-1.xx&oh=00_AT9rU4Z2UXt9rUpepZ5_TgSXuAUzPHAiFVua2N2QKE7I8Q&oe=61D5E5D7', 'https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/p526x395/269743289_4957844810902138_6580793924898517356_n.jpg?_nc_cat=106&ccb=1-5&_nc_sid=b9115d&_nc_ohc=h_ead3NGlEkAX8Wjw0Y&_nc_ht=scontent-tpe1-1.xx&oh=00_AT_0kRXxoklpHK-kAyhAIITU8k9UK3ayh7jCFulKjBIdXw&oe=61D5082A', 'https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/247612781_5102232496459582_742757824766615851_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=b9115d&_nc_ohc=TjNZXCDBvy4AX-mNXpk&tn=zR0b_NgGnqoqz_MS&_nc_ht=scontent-tpe1-1.xx&oh=00_AT8LauWmpY1JMQybYPe3upgCOCoQHa5id5DYKErrFio0mQ&oe=61D57382', 'https://scontent-tpe1-1.xx.fbcdn.net/v/t1.6435-9/117376075_3592009087477116_6595993419837670648_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=b9115d&_nc_ohc=Zpxj81pzNC0AX-q5Afs&_nc_oc=AQmmsvdDxpBnqxAO0-X_8xYQG75007tnSeZdSRQrXd7sWzWImcLh0_h2f3z6RQusITY&_nc_ht=scontent-tpe1-1.xx&oh=00_AT8usgujTM1cG0OO6BheZZ8uAKnIlbO-MhhsrTwbFUi59w&oe=61F5A991', 'https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/266087412_1944958172351349_7706700213881688288_n.jpg?_nc_cat=102&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=cS-D6fP8R0oAX-tiSh0&_nc_ht=scontent-tpe1-1.xx&oh=00_AT-xH92-HJMfmVpYsDKCTgoJRdl3NvPhJ0tGLoE3Y4qfzg&oe=61D676F2', 'https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/261827425_4664592700228655_914681131821903724_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=b9115d&_nc_ohc=d0GlfXf9vccAX8_RBB_&_nc_ht=scontent-tpe1-1.xx&oh=00_AT_AMURTxQjqGYxw8AUzLSy9iJmcUvqHZHxHwOrusu5o2g&oe=61D4F1E7' ,'https://cdn.sportz.im/2020.9.11_200912.jpg' ,'https://live.staticflickr.com/65535/49813710431_735ac752c3_z.jpg','https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/p526x395/252948124_434732661342738_2392610925427482857_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=730e14&_nc_ohc=xMvS6fk8N0wAX929ob2&_nc_ht=scontent-tpe1-1.xx&oh=00_AT-73UNIu0AXx_ajZJ8n9Stc3eTqSO4OvSeZ9q4qVb1rgA&oe=61D4A5B4','https://i.ytimg.com/vi/xMQrkRlRVgc/maxresdefault.jpg', 'https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/p526x296/269714353_286528000186113_49681508328846717_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=825194&_nc_ohc=tyPd-VKIg7QAX8stjwq&_nc_ht=scontent-tpe1-1.xx&oh=00_AT9fEEIdKAA_1el98XU8cZFuy8LGZtrC9XUUtV8937qq4g&oe=61D5D368','https://i.ytimg.com/vi/kPEwR7rc4iE/maxresdefault.jpg','https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/263808354_2849344212023214_5210529091381243947_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=b9115d&_nc_ohc=AjhQYjSM-HkAX9JAL3O&_nc_ht=scontent-tpe1-1.xx&oh=00_AT8gqNXdbPtz61c5l4K3zY2rf_O-kNehiM36RDe87HGaSQ&oe=61D566D1','https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/261324104_2483777701756378_6224551130191191908_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=b9115d&_nc_ohc=rPrGkdwZMxcAX-ciELC&_nc_ht=scontent-tpe1-1.xx&oh=00_AT-87_jLVAGzd-T4uFjS7KYo9f_Knda0BTwCk2tc-ehlcg&oe=61D57769','https://cache.pttweb.cc/imgur/chk6tyc/f/e63a9a04f62c484eb69751b4cd152aaa']
        reply_token = event.reply_token
        send_image_url(reply_token, members[random.randint(0,14)])
        self.go_back()


    def on_exit_state17(self):
        print("Leaving state17")