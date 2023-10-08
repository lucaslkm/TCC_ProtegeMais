username_helper="""
MDScreen:

    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        adaptive_height: True
        size_hint_x: .80
        pos_hint: {"center_x": .5, "center_y": .4}

        MDTextField:    
            hint_text: "Usuário"
            mode: "round"
            halign: "center"
            size_hint_x: None
            width:300

    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        adaptive_height: True
        size_hint_x: .80
        pos_hint: {"center_x": .5, "center_y": .3}

        MDTextField:    
            hint_text: "Senha"
            mode: "round"
            halign: "center"
            size_hint_x: None
            width:300

"""