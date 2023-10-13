
import bluetooth
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

class BluetoothScannerApp(App):
    def build(self):
        self.layout= RelativeLayout()
        self.button_1= Button(text= "Bluetooth", size_hint= (0.2, 0.2), pos_hint= {'x': 0.4, 'y': 0.2})
        self.button_3= Button(text= "Nhập IP", size_hint= (0.2, 0.2), pos_hint= {'x': 0.4, 'y': 0.8})
        self.button_2= Button(text= "Trở Về", size_hint= (0.1, 0.1), pos_hint= {'x': 0.1, 'y': 0.9})
        self.button_DONE_IP= Button(text= "DONE", size_hint= (0.1, 0.1), pos_hint= {'x': 0.4, 'y': 0.2})
        self.button_SEND_DONE= Button(text="OK",size_hint= (0.1, 0.1), pos_hint= {'x': 0.4, 'y': 0.4})
        self.button_send_data= Button(text="Gửi DATA", size_hint= (0.2, 0.2), pos_hint= {'x': 0.8, 'y': 0.8})
        self.send_data= TextInput(hint_text="Nhập Dữ Liệu Cần Gửi:...")
        self.IP_input= TextInput(hint_text="Mời Nhập IP:")
        self.label = Label(text= "Disconnect")
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.send_data)
        self.layout.add_widget(self.button_SEND_DONE)
        
        self.layout.add_widget(self.IP_input)
        self.layout.add_widget(self.button_1)
        self.layout.add_widget(self.button_2)
        self.layout.add_widget(self.button_3)       
        self.layout.add_widget(self.button_DONE_IP)
        self.layout.add_widget(self.button_send_data)
        
        
        self.button_DONE_IP.opacity=0
        self.button_DONE_IP.disabled=True
        self.send_data.opacity=0
        self.send_data.disabled=True
        self.IP_input.opacity=0
        self.IP_input.disabled=True
        self.button_2.opacity=0
        self.button_2.disabled=True
        self.label.opacity=1
        self.label.disabled=True
        self.button_SEND_DONE.opacity=0
        self.button_SEND_DONE.disabled=True
        self.button_1.bind(on_press= self.button_on_press)
        self.button_2.bind(on_press= self.press_button_2)
        self.button_3.bind(on_press= self.press_button_3)
        self.button_DONE_IP.bind(on_press= self.DONE_press)
        self.button_send_data.bind(on_press= self.Button_send_data)
        self.button_SEND_DONE.bind(on_press= self.Screen_Nomarl)
        return self.layout
    def button_on_press(self, instance):
        self.button_1.opacity= 0
        self.button_1.disabled=True
        self.button_2.opacity= 1
        self.button_2.disabled=False
        self.label.opacity= 1
        self.label.disabled=False
        self.button_3.opacity=0
        self.button_3.disabled=True
        self.button_SEND_DONE.opacity=0
        self.button_SEND_DONE.disabled=True
        self.button_send_data.opacity=0
        self.button_send_data.disabled=True
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        if nearby_devices:
            devices_text = "Các thiết bị Bluetooth gần đây:\n"
            for addr, name in nearby_devices:
                devices_text += f"Địa chỉ: {addr}\n, Tên: {name}\n"
            self.label.text = devices_text
        else:
            self.label.text = "Không tìm thấy thiết bị Bluetooth gần đây."
    def press_button_2(self, instance):
        self.button_1.opacity= 1
        self.button_1.disabled=False
        self.button_2.opacity= 0
        self.button_2.disabled=True
        self.label.opacity= 0
        self.label.disabled=True
        self.button_3.opacity=1
        self.button_3.disabled=False
        self.button_send_data.opacity=0
        self.button_send_data.disabled=True
        self.button_SEND_DONE.opacity=0
        self.button_SEND_DONE.disabled=True
        self.button_send_data.opacity=1
        self.button_send_data.disabled=False
    def press_button_3(self, instance):
        self.label.opacity= 0
        self.label.disabled=True
        self.button_1.opacity= 0
        self.button_1.disabled=True
        self.button_3.opacity= 0
        self.button_3.disabled=True
        self.button_2.opacity= 0
        self.button_2.disabled=True
        self.IP_input.opacity= 1
        self.IP_input.disabled=False
        self.button_send_data.opacity=0
        self.button_send_data.disabled=True
        self.button_DONE_IP.opacity=1
        self.button_DONE_IP.disabled=False
        self.button_SEND_DONE.opacity=0
        self.button_SEND_DONE.disabled=True
    def DONE_press(self, instance):
        self.button_SEND_DONE.opacity=0
        self.button_SEND_DONE.disabled=True
        self.save_ip= self.IP_input.text
        self.IP_input.opacity=0
        self.IP_input.disabled=True
        self.button_1.opacity= 1
        self.button_1.disabled=False
        self.button_2.opacity= 0
        self.button_2.disabled=True
        self.label.opacity= 1
        self.label.disabled=True
        self.button_DONE_IP.opacity=0
        self.button_DONE_IP.disabled=True
        self.button_3.opacity=1
        self.button_3.disabled=False
        device_address = self.IP_input.text
        self.button_send_data.opacity=1
        self.button_send_data.disabled=False
        
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((device_address, 1))  # Địa chỉ và cổng (port) của thiết bị Bluetooth
            self.label.text=f"Kết nối thành công đến {device_address}"
            sock.close()
        except Exception as e:
            self.label.text=f"Lỗi kết nối: {e}"
    def Button_send_data(self, instance):
        self.label.opacity=0
        self.label.disabled=True
        self.send_data.opacity=1
        self.send_data.disabled=False
        self.button_send_data.opacity=0
        self.button_send_data.disabled=True
        self.button_SEND_DONE.opacity=1
        self.button_SEND_DONE.disabled=False
        self.button_1.opacity= 0
        self.button_1.disabled=True
        self.button_3.opacity= 0
        self.button_3.disabled=True
        self.send_data.opacity=1
        self.send_data.disabled=False
        self.IP_input.opacity=0
        self.IP_input.disabled=True
    def Screen_Nomarl(self, instance):
        device_address = self.IP_input.text
        self.IP_input.opacity=0
        self.IP_input.disabled=True
        self.button_1.opacity= 1
        self.button_1.disabled=False
        self.button_2.opacity= 0
        self.button_2.disabled=True
        self.label.opacity= 1
        self.label.disabled=True
        self.button_DONE_IP.opacity=0
        self.button_DONE_IP.disabled=True
        self.button_3.opacity=1
        self.button_3.disabled=False
        self.button_send_data.opacity=1
        self.button_send_data.disabled=False
        self.button_SEND_DONE.opacity=0
        self.button_SEND_DONE.disabled=True
        self.send_data.opacity=0
        self.send_data.disabled=True
        try:
            
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((device_address, 1))  # Địa chỉ và cổng (port) của thiết bị Bluetooth

    # Gửi dữ liệu qua kết nối Bluetooth
            data_to_send = self.send_data.text
            sock.send(data_to_send)

    # Đóng kết nối
            sock.close()
            self.label.text=f"Dữ liệu {data_to_send} đã được gửi thành công."
        except Exception as e:
            self.label.text=f"Lỗi kết nối hoặc gửi dữ liệu: {e}"
if __name__ == "__main__":
    BluetoothScannerApp().run()
