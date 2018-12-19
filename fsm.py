from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '01'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '02'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '03'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '04'
        return False
    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '05'
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '06'
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '07'
        return False
    
    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '08'
        return False
    
    def is_going_to_state9(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '09'
        return False
    
    def is_going_to_state10(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '10'
        return False
    
    def is_going_to_state11(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '腳本'
        return False
    
    def is_going_to_state12(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '主題曲'
        return False

    def is_going_to_state21(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '腳本'
        return False
    
    def is_going_to_state22(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '主題曲'
        return False

    def is_going_to_state31(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '腳本'
        return False
    
    def is_going_to_state32(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '主題曲'
        return False

    def is_going_to_state41(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '腳本'
        return False
    
    def is_going_to_state42(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '主題曲'
        return False

    def is_going_to_state51(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '腳本'
        return False
    
    def is_going_to_state52(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '主題曲'
        return False

    def is_going_to_state61(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '腳本'
        return False
    
    def is_going_to_state62(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '主題曲'
        return False

    def is_going_to_state71(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '腳本'
        return False
    
    def is_going_to_state72(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '主題曲'
        return False

    def is_going_to_state81(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '腳本'
        return False
    
    def is_going_to_state82(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '主題曲'
        return False

    def is_going_to_state91(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '腳本'
        return False
    
    def is_going_to_state92(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '主題曲'
        return False

    def is_going_to_state101(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '腳本'
        return False
    
    def is_going_to_state102(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '主題曲'
        return False
    
    def is_going_to_stateback(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '回'
        return False
    
    def is_going_to_stateimg1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '海報'
        return False

    def is_going_to_stateimg2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '海報'
        return False
    
    def is_going_to_stateimg3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '海報'
        return False

    def is_going_to_stateimg4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '海報'
        return False

    def is_going_to_stateimg5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '海報'
        return False

    def is_going_to_stateimg6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '海報'
        return False

    def is_going_to_stateimg7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '海報'
        return False

    def is_going_to_stateimg8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '海報'
        return False
    
    def is_going_to_stateimg9(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '海報'
        return False

    def is_going_to_stateimg10(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '海報'
        return False





    def on_enter_stateimg1(self, event):
        print("I'm entering stateimage1")

        sender_id = event['sender']['id']
        responese =send_image_url(sender_id,'https://upload.wikimedia.org/wikipedia/zh/2/29/Conan1.jpg')
        #self.go_back()
    
    def on_exit_stateimg1(self,event):
        print('Leaving stateimage1')    
    

    def on_enter_stateimg2(self, event):
        print("I'm entering stateimage2")

        sender_id = event['sender']['id']
        responese =send_image_url(sender_id,'https://upload.wikimedia.org/wikipedia/zh/d/d9/Conan_2.jpg')
        #self.go_back()
    
    def on_exit_stateimg2(self,event):
        print('Leaving stateimage2')   

    def on_enter_stateimg3(self, event):
        print("I'm entering stateimage3")

        sender_id = event['sender']['id']
        responese =send_image_url(sender_id,'https://upload.wikimedia.org/wikipedia/zh/2/23/Conan3.jpg')
        #self.go_back()
    
    def on_exit_stateimg3(self,event):
        print('Leaving stateimage3')

    def on_enter_stateimg4(self, event):
        print("I'm entering stateimage4")

        sender_id = event['sender']['id']
        responese =send_image_url(sender_id,'https://upload.wikimedia.org/wikipedia/zh/4/4b/Conan_4.jpg')
        #self.go_back()
    
    def on_exit_stateimg4(self,event):
        print('Leaving stateimage4')
    
    def on_enter_stateimg5(self, event):
        print("I'm entering stateimage5")

        sender_id = event['sender']['id']
        responese =send_image_url(sender_id,'https://upload.wikimedia.org/wikipedia/zh/0/0a/Conan_5.jpg')
        #self.go_back()
    
    def on_exit_stateimg5(self,event):
        print('Leaving stateimage5')


    def on_enter_stateimg6(self, event):
        print("I'm entering stateimage6")

        sender_id = event['sender']['id']
        responese =send_image_url(sender_id,'https://upload.wikimedia.org/wikipedia/zh/5/5c/Conan_6.jpg')
        #self.go_back()
    
    def on_exit_stateimg6(self,event):
        print('Leaving stateimage6')
    
    def on_enter_stateimg7(self, event):
        print("I'm entering stateimage7")

        sender_id = event['sender']['id']
        responese =send_image_url(sender_id,'https://upload.wikimedia.org/wikipedia/zh/9/94/Conan_7.jpg')
        #self.go_back()
    
    def on_exit_stateimg7(self,event):
        print('Leaving stateimage7')

    def on_enter_stateimg8(self, event):
        print("I'm entering stateimage8")

        sender_id = event['sender']['id']
        responese =send_image_url(sender_id,'https://upload.wikimedia.org/wikipedia/zh/7/7c/Conan_8.jpg')
        #self.go_back()
    
    def on_exit_stateimg8(self,event):
        print('Leaving stateimage8')
    
    def on_enter_stateimg9(self, event):
        print("I'm entering stateimage9")

        sender_id = event['sender']['id']
        responese =send_image_url(sender_id,'https://upload.wikimedia.org/wikipedia/zh/9/98/Conan_9.jpg')
        #self.go_back()
    
    def on_exit_stateimg9(self,event):
        print('Leaving stateimage9')

    def on_enter_stateimg10(self, event):
        print("I'm entering stateimage10")

        sender_id = event['sender']['id']
        responese =send_image_url(sender_id,'https://upload.wikimedia.org/wikipedia/zh/f/f2/Conan_10.jpg')
        #self.go_back()
    
    def on_exit_stateimg10(self,event):
        print('Leaving stateimage10')
        
    
    def on_enter_state1(self,event):
        print("I'm entering state1")
        
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "引爆摩天樓")
        
    def on_exit_state1(self,event):
        print('Leaving state1')
    
    def on_enter_state11(self, event):
        print("I'm entering state11")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "古內一成")
        

    def on_exit_state11(self,event):
        print('Leaving state11')
    
    def on_enter_state12(self, event):
        print("I'm entering state12")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "生日快樂 演唱：杏子")
        #self.go_back()

    def on_exit_state12(self, event):
        print('Leaving state12')


    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "第十四號獵物")
        
    def on_exit_state2(self,event):
        print('Leaving state2')
    
    def on_enter_state21(self, event):
        print("I'm entering state21")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "古內一成")
        

    def on_exit_state21(self,event):
        print('Leaving state21')
    
    def on_enter_state22(self, event):
        print("I'm entering state12")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "彷彿回到少女時代 演唱：ZARD")
        #self.go_back()

    def on_exit_state22(self, event):
        print('Leaving state22')




    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "世紀末的魔術師")
        
    def on_exit_state3(self,event):
        print('Leaving state3')
    
    def on_enter_state31(self, event):
        print("I'm entering state31")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "古內一成")
        

    def on_exit_state31(self,event):
        print('Leaving state31')
    
    def on_enter_state32(self, event):
        print("I'm entering state32")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "ONE 演唱：B'z")
        #self.go_back()

    def on_exit_state32(self, event):
        print('Leaving state32')
    
    
    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "瞳孔中的暗殺者")
        
    def on_exit_state4(self,event):
        print('Leaving state4')
    
    def on_enter_state41(self, event):
        print("I'm entering state41")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "古內一成")
        

    def on_exit_state41(self,event):
        print('Leaving state41')
    
    def on_enter_state42(self, event):
        print("I'm entering state42")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "因為有你 演唱：小松未步")
        #self.go_back()

    def on_exit_state42(self, event):
        print('Leaving state42')

    def on_enter_state5(self, event):
        print("I'm entering state5")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "往天國的倒數計時")
        
    def on_exit_state5(self,event):
        print('Leaving state5')
    
    def on_enter_state51(self, event):
        print("I'm entering state51")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "古內一成")
        

    def on_exit_state51(self,event):
        print('Leaving state51')
    
    def on_enter_state52(self, event):
        print("I'm entering state52")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Always 演唱：倉木麻衣")
        #self.go_back()

    def on_exit_state52(self, event):
        print('Leaving state52')
    
    def on_enter_state6(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "貝克街的亡靈")
        
    def on_exit_state6(self,event):
        print('Leaving state6')
    
    def on_enter_state61(self, event):
        print("I'm entering state61")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "野澤尚")
        

    def on_exit_state61(self,event):
        print('Leaving state61')
    
    def on_enter_state62(self, event):
        print("I'm entering state62")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Everlasting 演唱：B'z")
        #self.go_back()

    def on_exit_state62(self, event):
        print('Leaving state62')



    def on_enter_state7(self, event):
        print("I'm entering state7")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "迷宮的十字路")
        
    def on_exit_state7(self,event):
        print('Leaving state7')
    
    def on_enter_state71(self, event):
        print("I'm entering state71")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "古內一成")
        

    def on_exit_state71(self,event):
        print('Leaving state71')
    
    def on_enter_state72(self, event):
        print("I'm entering state72")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Time after time~ 在落花紛飛的街道上～ 演唱：倉木麻衣")
       # self.go_back()

    def on_exit_state72(self, event):
        print('Leaving state72')


    
    def on_enter_state8(self, event):
        print("I'm entering state8")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "銀翼的奇術師")
        
    def on_exit_state8(self,event):
        print('Leaving state8')
    
    def on_enter_state81(self, event):
        print("I'm entering state81")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "古內一成")
        

    def on_exit_state81(self,event):
        print('Leaving state81')
    
    def on_enter_state82(self, event):
        print("I'm entering state82")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Dream X Dream 演唱：愛內里菜")
        #self.go_back()

    def on_exit_state82(self, event):
        print('Leaving state82')


    def on_enter_state9(self, event):
        print("I'm entering state9")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "水平線上的陰謀")
        
    def on_exit_state9(self,event):
        print('Leaving state9')
    
    def on_enter_state91(self, event):
        print("I'm entering state91")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "古內一成")
        

    def on_exit_state91(self,event):
        print('Leaving state91')
    
    def on_enter_state92(self, event):
        print("I'm entering state92")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "宛如等待夏日的風帆 演唱：ZARD")
        #self.go_back()

    def on_exit_state92(self, event):
        print('Leaving state92')

    def on_enter_state10(self, event):
        print("I'm entering state10")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "偵探們的鎮魂歌")
        
    def on_exit_state10(self,event):
        print('Leaving state10')
    
    def on_enter_state101(self, event):
        print("I'm entering state101")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "伯原寬司")
        

    def on_exit_state101(self,event):
        print('Leaving state101')
    
    def on_enter_state102(self, event):
        print("I'm entering state102")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "唯一絕不動搖的東西 演唱：B'z")
        #self.go_back()

    def on_exit_state102(self, event):
        print('Leaving state102')

    def on_enter_stateback(self, event):
        print("I'm entering stateback")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "ok")
        self.go_back()

    def on_exit_stateback(self):
        print('Leaving stateback')




    