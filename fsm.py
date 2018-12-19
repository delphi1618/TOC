from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def to_start1(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return True
        return False

    def to_music1(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'music'
        return False

    def to_fun1(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'video'
        return False

    def to_joke1(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'joke'
        return False

    def to_music2(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'yes'
        return False

    def to_ch1(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'chinese'
        return False

    def to_ch2(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'yes'
        return False

    def to_ch3(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'yes'
        return False

    def to_jp1(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'japanese'
        return False

    def to_jp2(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'yes'
        return False

    def to_jp3(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'ok'
        return False

    def to_joke2(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'yes'
        return False

    def to_joke3(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'yes'
        return False

    def to_joke4(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return True
        return False

    def to_fun2(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'yes'
        return False

    def to_fun3(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'yes'
        return False

    def to_fun4(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return True
        return False

    def to_beg(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'no'
        return False

    def on_enter_start1(self, event):
        print("I'm entering start1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Hello! I'm the bot trying to make you happy. If you want to listen to music, type music. If you want to watch some funny videos, type video. If you want to see some jokes, type joke.")

    def on_enter_music1(self, event):
        print("I'm entering music1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Do you really want to listen to music? If so, type yes. If not, type no to return.")

    def on_enter_music2(self, event):
        print("I'm entering music2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Which kind of music do you want? type chinese for chinese music. type japanese for japanese music.")

    def on_enter_jp1(self, event):
        print("I'm entering jp1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://youtu.be/QohgME8ay8A")
        send_text_message(sender_id, "If you want to see the lyrics, type yes. If not, type no to return.")

    def on_enter_jp2(self, event):
        print("I'm entering jp2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "今だってそんなに/自信はないよ/踏み出せない時もあるよ/もし間違ってたり/繰り返しちゃったり/したらどうしようって/選ばないだけなら/不安はないね/だけど変わることも/ないよね/いつだった?　どうなった?/もうダメだって　全ておしまい/だってなってた　あの時何だった?　誰だった?/そんなんでも　なんとか/もう一度って思って進めたのは/2 u, yeah/信じてる　信じられてる/4 u, yeah/空だって　飛べる気がする/ただひとり　君のためなら")
        send_text_message(sender_id, "If you want to see the translation, type ok. If not, type no to return.")

    def on_enter_jp3(self, event):
        print("I'm entering jp3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Translation. HAHAHA! Just kidding. Let's start again!If you want to listen to music, type music. If you want to watch some funny videos, type video. If you want to see some jokes, type joke.")
        self.go_back()

    def on_enter_ch1(self, event):
        print("I'm entering jp1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://youtu.be/9oJoVtKoCzA")
        send_text_message(sender_id, "This one seems too old-fashioned. If you want a newer song, type yes. If not, type no to return.")

    def on_enter_ch2(self, event):
        print("I'm entering jp2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://youtu.be/OLimUac1_VU")
        send_text_message(sender_id, "Is this one better? HAHA If you want to listen to another song, type yes. If not, type no to return.")

    def on_enter_ch3(self, event):
        print("I'm entering jp3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "So sad... Actually, I don't like Chinese music. Let's start from the beginning!If you want to listen to music, type music. If you want to watch some funny videos, type video. If you want to see some jokes, type joke.")
        self.go_back()

    def on_enter_joke1(self, event):
        print("I'm entering jp1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "小明學校有一個同學叫李弘毅,有一天小明想找他找不到,就問小美:「李弘毅幾班？」他慢慢轉頭回答: 「DAIKIN」")
        send_text_message(sender_id, "If you want to see more jokes, type yes. If not, type no to return.")

    def on_enter_joke2(self, event):
        print("I'm entering jp1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "孩子第一天上學回來，父親問他可喜歡上學；孩子說：『我喜歡去上學，也喜歡放學，可是不喜歡中間的時間。』")
        send_text_message(sender_id, "If you want to see more jokes, type yes. If not, type no to return.")

    def on_enter_joke3(self, event):
        print("I'm entering jp1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "五歲的兒子第一次來動物園，走到黑天鵝區，看到黑天鵝時，高興地跟爸爸說：爸爸、爸爸、你看！薑母鴨！")
        send_text_message(sender_id, "If you want to see more jokes, type yes. If not, type no to return.")

    def on_enter_joke4(self, event):
        print("I'm entering jp1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "林北哪有那麼多時間陪你講笑話...")
        send_text_message(sender_id, "Let's start again! If you want to listen to music, type music. If you want to watch some funny videos, type video. If you want to see some jokes, type joke.")
        self.go_back()

    def on_enter_fun1(self, event):
        print("I'm entering jp1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://youtu.be/_iwOmOtyiEc")
        send_text_message(sender_id, "If you want to watch more videos, type yes. If not, type no to return.")

    def on_enter_fun2(self, event):
        print("I'm entering jp1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://youtu.be/8UHxneuLCRI")
        send_text_message(sender_id, "If you want to watch more videos, type yes. If not, type no to return.")

    def on_enter_fun3(self, event):
        print("I'm entering jp1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "https://youtu.be/DkXlUNCN6VM")
        send_text_message(sender_id, "If you want to watch more videos, type yes. If not, type no to return.")

    def on_enter_fun4(self, event):
        print("I'm entering jp1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "你如果都好好看完了表示眼睛該休息了!")
        send_text_message(sender_id, "Let's start again! If you want to listen to music, type music. If you want to watch some funny videos, type video. If you want to see some jokes, type joke.")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')
