from tkinter import *
from tkinter import simpledialog



class SmartDevice:
    """
    Base class representing a smart device.
    Provides functionality for turning devices on and off.
    """
    def __init__(self):
        self._switched_on = False
        
    def toggle_switch(self):
        self._switched_on = not self._switched_on
        
    def __str__(self):
        state = "on" if self._switched_on else "off"
        return f"{self.__class__.__name__} is {state}"

class SmartPlug(SmartDevice):
    def __init__(self, consumption_rate):
        super().__init__()
        if not (0 <= consumption_rate <= 150):
            raise ValueError(f" Invalid consumption rate: {consumption_rate} must be 0 - 150")
        self._consumption_rate = consumption_rate


    @property
    def consumption_rate(self):
        return self._consumption_rate
    
    @consumption_rate.setter
    def consumption_rate(self, new_rate):
        if 0 <= new_rate <= 150:
            self._consumption_rate = new_rate
        else:
            print(f"{new_rate} is invalid rate, consumption rate must be 0 - 150")
        
        
    def __str__(self):
        state = "on" if self._switched_on else "off"
        return f"SmartPlug is {state} with a consumption rate of {self.consumption_rate}"

class SmartAirFryer(SmartDevice):
    def __init__(self, cook_mode="Healthy"):
        super().__init__()
        self.cook_mode = cook_mode  

    @property
    def cook_mode(self):
        return self._cook_mode
    
    @cook_mode.setter
    def cook_mode(self, value):
        value = value[0].upper() + value[1:].lower()
        if value in ["Healthy", "Defrost", "Crispy"]:
            self._cook_mode = value
        else:
            raise ValueError("Cook mode must be 'Healthy', 'Defrost', or 'Crispy'.")


    def __str__(self):
        state = "on" if self._switched_on else "off"
        return f"SmartAirFryer is {state} with cook mode: {self.cook_mode}"




class SmartSpeaker(SmartDevice):
    def __init__(self, streaming="Amazon"):
        super().__init__()
        self._streaming = streaming
        
        
    @property
    def streaming(self):
        return self._streaming
    
    
    @streaming.setter
    def streaming(self, value):
        value = value[0].upper() + value[1:].lower()
        if value in ["Amazon", "Apple", "Spotify"]:
            self._streaming = value
        else:
            raise ValueError("Streaming service must be 'Amazon', 'Apple', or 'Spotify'.")

    
    def __str__(self):
        state = "on" if self._switched_on else "off"
        return f"SmartSpeaker is {state} streaming from {self.streaming}"


class SmartHome:
    """
    Stores and manages multiple smart devices.
    Supports adding, removing, updating and controlling devices.
    """
    def __init__(self, max_items=5):
        self._max_items = max_items
        self._devices = []
        
    def add_device(self, device: object):
    """
    Add a device to the smart home system.
    """
        if len(self._devices) >= self._max_items:
            raise ValueError(f"Can't add more than {self._max_items} devices.")
        self._devices.append(device)
        
    def remove_device(self, index: int):
        
        if 0 <= index < len(self._devices):
            self._devices.pop(index)
        else:
            raise IndexError("Device index out of range.")
        
    def get_device(self, index:int):
        if 0 <= index < len(self._devices):
            return self._devices[index]
        else:
            raise IndexError("Device index out of range.")
        
    def toggle_device(self, index: int):
        self._devices[index].toggle_switch()
        
    def toggle_device(self, index: int):
        self._devices[index].toggle_switch()

        
    def update_option(self, index: int, value):
        if 0 <= index < len(self._devices):
            device = self._devices[index]
            
            if isinstance(device, SmartAirFryer):
                device.cook_mode = value
            elif isinstance(device, SmartSpeaker):
                device.streaming = value
            elif isinstance (device, SmartPlug):
                device.consumption_rate = value
            else:
                print("Invalid type of device.")
        else:
            raise IndexError("Device index out of range.")
            
        
    def switch_all_on(self):
        for device in self._devices:
            if not device._switched_on:
                device.toggle_switch()
                

    def switch_all_off(self):
        for device in self._devices:
            if device._switched_on:
                device.toggle_switch()
            
    def __str__(self):
        device_info = ""
        for i, device in enumerate(self._devices):
            device_info += f"{i+1}- {device}\n"
        return f"SmartHome with {len(self._devices)} devices: \n{device_info}"
    

def test_smart_plug():
    smart_plug = SmartPlug(45)
    print(smart_plug)
    
    smart_plug.toggle_switch()    
    print(smart_plug)
    
    smart_plug.consumption_rate = 75
    print(smart_plug)

    smart_plug.toggle_switch()    
    print(smart_plug)
    
    smart_plug.consumption_rate = 200
    print(smart_plug)
    
# test_smart_plug()

def test_custom_devices():
    air_fryer = SmartAirFryer()
    speaker = SmartSpeaker()
    
    print(air_fryer)
    air_fryer.toggle_switch()
    print(air_fryer)
    air_fryer.cook_mode = "Crispy"
    print(air_fryer)
    
    print(speaker)
    speaker.toggle_switch()
    print(speaker)
    speaker.streaming = "Spotify"
    print(speaker)
    
    try:
        air_fryer.cook_mode = "Boil"  
    except ValueError as e:
        print(e)
    
    try:
        speaker.streaming = "YouTube"  
    except ValueError as e:
        print(e)

# test_custom_devices()
        
def test_smart_home():
    smart_plug = SmartPlug(50)  
    air_fryer = SmartAirFryer()
    speaker = SmartSpeaker()

    smart_home = SmartHome(3)

    print("Adding devices to the SmartHome system:")
    smart_home.add_device(smart_plug)
    smart_home.add_device(air_fryer)
    smart_home.add_device(speaker)

    print(smart_home)

    print("\nRetrieving devices:")
    retrieved_plug = smart_home.get_device(0)
    retrieved_air_fryer = smart_home.get_device(1)
    retrieved_speaker = smart_home.get_device(2)

    print(f"Device at index 0: {retrieved_plug}")
    print(f"Device at index 1: {retrieved_air_fryer}")
    print(f"Device at index 2: {retrieved_speaker}")

    print("\nToggling each device individually:")
    smart_home.toggle_device(0)  
    smart_home.toggle_device(1) 
    smart_home.toggle_device(2)  

    print(smart_home)  

    print("\nSwitching all devices on and off:")
    smart_home.switch_all_on()
    print(smart_home)
    smart_home.switch_all_off()
    print(smart_home)

    try:
        smart_home.add_device(SmartAirFryer())  
        print("\nAdded another device:")
        print(smart_home)
    except ValueError as e:
        print(f"Error adding device: {e}")

    try:
        smart_home.add_device(SmartSpeaker())  
    except ValueError as e:
        print(f"Error: {e}")
        
    print("\nUpdating the option attributes:")
    try:
        smart_home.update_option(0, 75) 
        print(smart_home)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        smart_home.update_option(0, -10)  
    except ValueError as e:
        print(f"Error: {e}")

    try:
        smart_home.update_option(1, "Crispy")  
        print(smart_home)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        smart_home.update_option(1, "Boil") 
    except ValueError as e:
        print(f"Error: {e}")

    try:
        smart_home.update_option(2, "Spotify") 
        print(smart_home)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        smart_home.update_option(2, "YouTube")  
    except ValueError as e:
        print(f"Error: {e}")

    print("\nRemoving a device from the system:")
    smart_home.remove_device(0) 
    print(smart_home)

    try:
        smart_home.remove_device(5)  
    except IndexError as e:
        print(f"Error: {e}")

    try:
        smart_home.remove_device(-1) 
    except IndexError as e:
        print(f"Error: {e}")

    print("\nFinal state of SmartHome after all operations:")
    print(smart_home)

# test_smart_home()
  

class SmartHomeApp:
    def __init__(self, root, smart_home):
        self.root = root
        self.root.title("Smart Home Control Panel")
        self.root.configure(bg="#cfcfcf")
        self.root.geometry("700x400")

        # Use the existing SmartHome instance
        self.smart_home = smart_home
        self.create_widgets()

        
    def create_widgets(self):
        self.clear_widgets()  # Clear existing widgets first

        # **Top Frame (Switch All On/Off)**
        top_frame = Frame(self.root, bg="#cfcfcf")
        top_frame.pack(fill="x", pady=10)

        btn_all_on = Button(
            top_frame,
            text="Turn All On",
            width=15,
            height=2,
            padx=20,
            pady=5,
            borderwidth=2,
            highlightbackground="black",
            command=self.turn_all_on,
        )
        
        btn_all_on.pack(side=LEFT, padx=60)

        btn_all_off = Button(
            top_frame,
            text="Turn All Off",
            width=15,
            height=2,
            padx=20,
            pady=5,
            borderwidth=2,
            highlightbackground="black",
            command=self.turn_all_off,
        )
        
        btn_all_off.pack(side=RIGHT, padx=80)

        # Device Frames (for listing devices)
        self.devices_frame = Frame(self.root, bg="#cfcfcf")
        self.devices_frame.pack(pady=10, fill="both", expand=True)

        self.device_labels = []
        self.toggle_buttons = []
        self.edit_buttons = []
        self.delete_buttons = []

        for index, device in enumerate(self.smart_home._devices):
            device_label = Label(self.devices_frame, text=str(device), bg="#cfcfcf", padx=10)
            device_label.grid(row=index, column=0, sticky=W, padx=10)
            self.device_labels.append(device_label)

            btn_toggle = Button(
                self.devices_frame,
                text="Toggle",
                borderwidth=1,
                highlightbackground="black",
                command=lambda i=index: self.toggle_device(i),
            )
            
            btn_toggle.grid(row=index, column=1, padx=5)

            btn_edit = Button(
                self.devices_frame,
                text="Edit",
                borderwidth=1,
                highlightbackground="black",
                command=lambda i=index: self.edit_device(i)
            )
            
            btn_edit.grid(row=index, column=2, padx=5)

            btn_delete = Button(
                self.devices_frame,
                text="Delete",
                borderwidth=1,              
                highlightbackground="black",
                command=lambda i=index: self.delete_device(i)
            )
            
            btn_delete.grid(row=index, column=3, padx=5)

        # Bottom Frame (Add Button)
        bottom_frame = Frame(self.root, bg="#cfcfcf")
        bottom_frame.pack(pady=10)

        btn_add = Button(
            bottom_frame,
            text="Add Device",
            borderwidth=1,              
            highlightbackground="black",            
            command=self.add_device)
        btn_add.pack()

        
    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        


    def turn_all_on(self):
        self.smart_home.switch_all_on()
        print(self.smart_home)
        self.create_widgets()



    def turn_all_off(self):
        self.smart_home.switch_all_off()
        print(self.smart_home)
        self.create_widgets()
        
    
    def toggle_device(self, index):
        self.smart_home.toggle_device(index)
        print(self.smart_home)
        self.create_widgets()
    
    def delete_device(self, index):
        self.smart_home.remove_device(index)
        print(self.smart_home)
        self.create_widgets()
        
    def edit_device(self, index):
        device = self.smart_home.get_device(index)
        self.create_widgets()
      
        if isinstance(device, SmartPlug):
            new_value = simpledialog.askinteger("Edit SmartPlug", "Enter new consumption rate (0-150):", minvalue=0, maxvalue=150)
            if new_value is not None:
                device.consumption_rate = new_value  # This will update the device's consumption rate
        elif isinstance(device, SmartAirFryer):
            new_value = simpledialog.askstring("Edit SmartAirFryer", "Enter new cook mode (Healthy, Defrost, Crispy):")
            new_value = new_value[0].upper() + new_value[1:].lower()

            if new_value in ["Healthy", "Defrost", "Crispy"]:
                device.cook_mode = new_value  # This will update the device's cook mode
        elif isinstance(device, SmartSpeaker):
            new_value = simpledialog.askstring("Edit SmartSpeaker", "Enter new streaming service (Amazon, Apple, Spotify):")
            new_value = new_value[0].upper() + new_value[1:].lower()
            
            if new_value in ["Amazon", "Apple", "Spotify"]:
                device.streaming = new_value  # This will update the device's streaming service
        else:
            print("Invalid device type")
        
        print(self.smart_home)
        self.create_widgets()  # Refresh the widgets to reflect the changes

        
    

    def add_device(self):
        device_type = simpledialog.askstring("Add Device", "Enter device type (Plug, AirFryer, Speaker):")
        device_type = device_type.lower()  # Ensure input is cleaned up
        if device_type == "plug":
            consumption = simpledialog.askinteger("New SmartPlug", "Enter consumption rate (0-150):", minvalue=0, maxvalue=150)
            if consumption is not None:
                self.smart_home.add_device(SmartPlug(consumption))
        elif device_type == "airfryer":
            mode = simpledialog.askstring("New SmartAirFryer", "Enter cook mode (Healthy, Defrost, Crispy):")
            mode = mode[0].upper() + mode[1:].lower()
            if mode in ["Healthy", "Defrost", "Crispy"]:
                self.smart_home.add_device(SmartAirFryer(mode))
        elif device_type == "speaker":
            streaming = simpledialog.askstring("New SmartSpeaker", "Enter streaming service (Amazon, Apple, Spotify):")
            streaming = streaming[0].upper() + streaming[1:].lower()

            if streaming in ["Amazon", "Apple", "Spotify"]:
                self.smart_home.add_device(SmartSpeaker(streaming))
        else:
            print("Invalid device type")
        self.create_widgets()

        
    
    def refresh_labels(self):
        for i, device in enumerate(self.smart_home._devices):
            self.device_labels[i].config(text=device)
    
    def run(self):
        self.create_widgets()
        self.root.mainloop()



def test_smart_home_app():

    home3=SmartHome(10)
    home3.add_device(SmartAirFryer())
    home3.add_device(SmartSpeaker())
    home3.add_device(SmartPlug(45))

    #print("\n State of SmartHome after creating devices:")
    print(home3)
    win = Tk()
    app = SmartHomeApp(win, home3)
    app.run()
    
    

test_smart_home_app()



        
