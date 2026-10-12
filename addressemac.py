# -*- coding: utf-8 -*-
# Base de données OUI étendue (Constructeurs)
vendors = {
    # ==========================================
    # VIRTUALIZATION / CLOUD
    # ==========================================
    # VMware
    "00-05-69": "VMware", "00-0C-29": "VMware", "00-50-56": "VMware", "00-1C-14": "VMware",
    # Microsoft Hyper-V
    "00-15-5D": "Microsoft Hyper-V", "00-03-FF": "Microsoft VPC", "00-12-5A": "Microsoft Azure",
    # Oracle / VirtualBox
    "08-00-27": "Oracle VirtualBox",
    # Docker / Containers
    "02-42-AC": "Docker Container", 
    # Others
    "00-16-3E": "Xen", "52-54-00": "QEMU/KVM", "00-1C-42": "Parallels", "00-21-F6": "Risoul (Virtual)",

    # ==========================================
    # SINGLE BOARD COMPUTERS (SBC) & MAKER
    # ==========================================
    # Raspberry Pi (Foundation)
    "DC-A6-32": "Raspberry Pi", "B8-27-EB": "Raspberry Pi", "E4-5F-01": "Raspberry Pi", 
    "D8-3A-DD": "Raspberry Pi", "28-CD-C1": "Raspberry Pi", "2C-CF-67": "Raspberry Pi",
    # Arduino
    "90-A2-DA": "Arduino", "F0-D1-A0": "Arduino",
    # Espressif (ESP8266 / ESP32 - Trés courant en IoT DIY)
    "18-FE-34": "Espressif", "24-0A-C4": "Espressif", "24-6F-28": "Espressif", "24-B2-DE": "Espressif",
    "30-AE-A4": "Espressif", "5C-CF-7F": "Espressif", "60-01-94": "Espressif", "84-F3-EB": "Espressif",
    "A0-20-A6": "Espressif", "AC-67-B2": "Espressif", "EC-FA-BC": "Espressif", "80-7D-3A": "Espressif",

    # ==========================================
    # IOT & SMART HOME (DOMOTIQUE)
    # ==========================================
    # Philips Hue (Signify)
    "00-17-88": "Philips Hue", "EC-B5-FA": "Philips Hue",
    # Amazon (Echo/Alexa/Ring)
    "00-3E-E1": "Amazon (Echo)", "74-C2-46": "Amazon", "F0-D2-F1": "Amazon", "44-65-0D": "Amazon",
    "88-71-E5": "Amazon", "68-54-FD": "Amazon", "34-D2-70": "Amazon", "AC-E3-42": "Ring (Amazon)",
    # Google (Nest/Home)
    "18-B4-30": "Google Nest", "64-16-66": "Google Nest", "D8-EB-46": "Google", 
    # Tuya Smart (Prises connectées chinoises génériques)
    "10-5A-17": "Tuya Smart", "50-8A-06": "Tuya Smart", "D4-D2-D6": "Tuya Smart",
    # Shelly (Allterco)
    "34-94-54": "Shelly/Allterco", "84-CC-A8": "Shelly/Allterco",
    # Sonos
    "00-0E-58": "Sonos", "34-7E-5C": "Sonos", "48-A6-B8": "Sonos", "5C-AA-FD": "Sonos", "94-9F-3E": "Sonos",
    # Belkin / Wemo
    "14-91-82": "Belkin (Wemo)", "EC-1A-59": "Belkin", "94-10-3E": "Belkin",
    # Dyson
    "C0-D0-12": "Dyson (Purifier)",
    # iRobot (Roomba)
    "50-14-79": "iRobot", "D0-C5-D3": "iRobot",

    # ==========================================
    # SMART TV & MEDIA
    # ==========================================
    # LG
    "00-1C-62": "LG Electronics", "04-67-40": "LG Electronics", "14-7D-C5": "LG Electronics", 
    "3C-BD-D8": "LG Electronics", "A8-23-FE": "LG Electronics", "C4-36-6C": "LG Electronics",
    # Roku
    "00-0D-4B": "Roku", "20-82-C0": "Roku", "88-DE-A9": "Roku", "AC-AE-19": "Roku", "D8-31-34": "Roku",
    # Vizio
    "00-26-87": "Vizio", "14-8F-C6": "Vizio",
    # Nvidia (Shield)
    "00-04-4B": "Nvidia", "48-B0-2D": "Nvidia",

    # ==========================================
    # SECURITY & CAMERAS
    # ==========================================
    # Hikvision
    "10-12-FB": "Hikvision", "44-32-C8": "Hikvision", "A4-14-37": "Hikvision", "C4-2F-90": "Hikvision",
    # Dahua
    "38-AF-29": "Dahua", "90-02-A9": "Dahua", "BC-32-5F": "Dahua",
    # Axis Communications
    "00-40-8C": "Axis", "AC-CC-8E": "Axis",
    # Arlo
    "A0-04-60": "Netgear (Arlo)",

    # ==========================================
    # NAS & STORAGE
    # ==========================================
    # Synology
    "00-11-32": "Synology",
    # QNAP
    "00-08-9B": "QNAP", "24-5E-BE": "QNAP", 
    # Asustor
    "10-BF-48": "Asustor", "20-19-03": "Asustor",
    # Western Digital
    "00-90-A9": "Western Digital", 

    # ==========================================
    # PC COMPONENTS (Motherboards, NICs)
    # ==========================================
    # Dell
    "00-14-22": "Dell", "00-16-D3": "Dell", "00-1C-23": "Dell", "F0-4D-A2": "Dell", "14-FE-B5": "Dell",
    # HP
    "9C-8E-99": "HP", "3C-D9-2B": "HP", "00-1B-78": "HP", "D8-9E-F3": "HP", "FC-3F-DB": "HP",
    # Intel
    "00-11-11": "Intel", "00-1B-21": "Intel", "00-13-20": "Intel", "00-A0-C9": "Intel", 
    "00-15-00": "Intel", "00-1E-64": "Intel", "00-22-FA": "Intel", "00-24-D7": "Intel", "80-86-F2": "Intel",
    # Asus
    "00-24-8C": "Asus", "AC-22-0B": "Asus", "F0-79-59": "Asus", "04-92-26": "Asus", "2C-4D-54": "Asus", "D8-43-AE": "Asus",
    # Gigabyte
    "FC-AA-14": "Giga-Byte", "E0-D5-5E": "Giga-Byte", "1C-1B-0D": "Giga-Byte",
    # MSI
    "4C-CC-6A": "MSI", "D8-CB-8A": "MSI", "30-9C-23": "MSI", "00-16-17": "MSI", "D8-5E-D3": "MSI",
    # ASRock
    "70-85-C2": "ASRock", "BC-5F-F4": "ASRock",
    # Realtek (Très commun sur les PC portables)
    "00-E0-4C": "Realtek", "00-00-5E": "ICANN (Reserved)",

    # ==========================================
    # NETWORKING EQUIPMENT (PRO & CONSUMER)
    # ==========================================
    # Ubiquiti (UniFi)
    "F0-9F-C2": "Ubiquiti", "74-83-C2": "Ubiquiti", "B4-FB-E4": "Ubiquiti", "00-15-6D": "Ubiquiti", 
    "00-27-22": "Ubiquiti", "60-22-32": "Ubiquiti", "78-8A-20": "Ubiquiti", "E0-63-DA": "Ubiquiti",
    # TP-Link
    "14-CC-20": "TP-Link", "50-C7-BF": "TP-Link", "F4-F2-6D": "TP-Link", "C0-25-E9": "TP-Link", 
    "60-32-B1": "TP-Link", "98-DE-D0": "TP-Link", "7C-8B-CA": "TP-Link", "E8-48-B8": "TP-Link",
    # Netgear
    "E8-9F-80": "Netgear", "A0-40-A0": "Netgear", "2C-B0-5D": "Netgear", "9C-D3-6D": "Netgear",
    # Cisco (Enterprise)
    "00-18-01": "Cisco", "00-25-45": "Cisco", "00-00-0C": "Cisco", "00-01-42": "Cisco", 
    "00-08-E3": "Cisco", "00-1A-A1": "Cisco", "00-22-55": "Cisco",
    # MikroTik (RouterOS)
    "08-55-31": "MikroTik", "18-FD-74": "MikroTik", "2C-C8-1B": "MikroTik", "48-8F-5A": "MikroTik",
    "64-D1-54": "MikroTik", "6C-3B-6B": "MikroTik", "CC-2D-E0": "MikroTik", "E4-8D-8C": "MikroTik",
    # Fortinet (Security)
    "00-09-0F": "Fortinet", "08-5B-0E": "Fortinet", "70-4C-A5": "Fortinet", "90-6C-AC": "Fortinet",
    # Palo Alto Networks
    "00-1B-17": "Palo Alto", "08-66-98": "Palo Alto",
    # Juniper Networks
    "00-05-85": "Juniper", "00-10-DB": "Juniper", "40-B4-F0": "Juniper",
    # Linksys
    "00-03-7F": "Linksys", "C4-41-1E": "Linksys",
    # D-Link
    "00-05-5D": "D-Link", "00-0D-88": "D-Link", "14-D6-4D": "D-Link", "90-94-E4": "D-Link",
    # Aruba (HPE)
    "00-0B-86": "Aruba", "00-1A-1E": "Aruba", "20-4C-03": "Aruba", "94-F1-28": "Aruba",

    # ==========================================
    # ISP BOXES / ROUTERS (FRANCE & GLOBAL)
    # ==========================================
    # Sagemcom (Livebox, SFR Box, etc.)
    "A0-1B-29": "Sagemcom", "F4-CA-E5": "Sagemcom", "18-62-2C": "Sagemcom", "44-CE-7D": "Sagemcom",
    # Arcadyan (Livebox, Bouygues)
    "1C-C6-3C": "Arcadyan", "88-03-55": "Arcadyan",
    # Orange (Direct)
    "00-19-70": "Orange", "6C-2E-85": "Orange", "00-12-7F": "Orange",
    # Free / Freebox
    "E4-9E-12": "Freebox", "00-07-CB": "Freebox", "00-24-D4": "Freebox", "14-0C-76": "Freebox",
    # SFR
    "E0-A1-D7": "SFR", "00-17-33": "Neuf/SFR",
    # Bouygues Telecom
    "00-1F-9F": "Bouygues", "34-27-92": "Bouygues",
    # Starlink
    "98-ED-5C": "Starlink", "24-F8-63": "Starlink", "74-24-9F": "Starlink",

    # ==========================================
    # MOBILE DEVICES (SMARTPHONES / TABLETS)
    # ==========================================
    # Apple (Selection des plus courants, il y en a des milliers)
    "00-23-12": "Apple", "00-25-00": "Apple", "00-1F-F3": "Apple", "BC-92-6B": "Apple", 
    "F0-18-98": "Apple", "DC-2B-2A": "Apple", "A4-D1-8C": "Apple", "AC-BC-32": "Apple", 
    "14-20-5E": "Apple", "14-99-E2": "Apple", "28-6A-B8": "Apple", "34-36-3B": "Apple",
    "40-4D-7F": "Apple", "48-43-7C": "Apple", "60-03-08": "Apple", "88-63-DF": "Apple",
    "98-00-C6": "Apple", "A8-5C-2C": "Apple", "C8-1E-E7": "Apple", "E4-9A-79": "Apple",
    "F4-0F-24": "Apple", "F8-1E-DF": "Apple", "FC-25-3F": "Apple", "00-17-F2": "Apple",
    # Samsung (Selection)
    "00-12-47": "Samsung", "00-15-99": "Samsung", "A0-B4-A5": "Samsung", "AC-5F-3E": "Samsung",
    "24-4B-03": "Samsung", "30-07-4D": "Samsung", "34-14-5F": "Samsung", "38-01-95": "Samsung",
    "50-01-D9": "Samsung", "5C-0A-5B": "Samsung", "78-00-9E": "Samsung", "84-25-DB": "Samsung",
    "8C-71-F8": "Samsung", "90-18-7C": "Samsung", "9C-02-98": "Samsung", "BC-20-A4": "Samsung",
    # Xiaomi
    "00-9E-C8": "Xiaomi", "14-F6-5A": "Xiaomi", "AC-F7-F3": "Xiaomi", "50-EC-50": "Xiaomi",
    "64-CC-2E": "Xiaomi", "F4-F5-DB": "Xiaomi", "F8-A4-5F": "Xiaomi",
    # Huawei
    "00-1E-10": "Huawei", "48-46-C1": "Huawei", "AC-E8-7B": "Huawei", "E8-CD-2D": "Huawei",
    "20-54-FA": "Huawei", "58-1F-28": "Huawei",
    # OnePlus
    "64-A2-F9": "OnePlus", "A8-9C-ED": "OnePlus",
    # Oppo
    "4C-18-9A": "Oppo", "84-AA-9C": "Oppo",
    # Sony
    "18-C0-4D": "Sony Mobile", "F0-BF-97": "Sony Mobile",
    # Google (Pixel)
    "3C-5A-B4": "Google Pixel", "54-60-09": "Google Pixel", "70-3A-CB": "Google Pixel",

    # ==========================================
    # GAMING CONSOLES
    # ==========================================
    # Nintendo (Switch / Wii)
    "B8-5F-98": "Nintendo Switch", "98-B6-E9": "Nintendo Switch", "00-1C-BE": "Nintendo",
    "7C-BB-8A": "Nintendo", "94-58-CB": "Nintendo",
    # PlayStation (Sony)
    "48-17-4C": "PlayStation", "00-D9-D1": "PlayStation", "00-04-1F": "PlayStation",
    "10-48-B1": "PlayStation", "70-9E-29": "PlayStation", "F8-46-1C": "PlayStation",
    # Xbox (Microsoft)
    "50-1E-2D": "Xbox", "C8-3F-26": "Xbox", "28-18-78": "Xbox", "44-16-22": "Xbox",
    "7C-1E-52": "Xbox", "98-5F-D3": "Xbox",
    # Valve (Steam Deck)
    "F8-0D-60": "Valve (Steam Deck)",

    # ==========================================
    # PRIVACY / RANDOMIZED MACs
    # ==========================================
    # Les adresses MAC aléatoires (Android/iOS modernes) ont souvent le 
    # second caractère qui est 2, 6, A ou E. 
    # C'est dur à filtrer par liste, mais voici quelques exemples génériques :
    "02-00-00": "Private/Randomized", "06-00-00": "Private/Randomized",
    "0A-00-00": "Private/Randomized", "0E-00-00": "Private/Randomized",

    # ==========================================
    # ADDED FROM YOUR SCAN (IMAGES)
    # ==========================================
    # Gateway / Box Internet (Image 192.168.1.1)
    # "74-24-9F": "Technicolor (ISP Box)", # Removed duplicate (Starlink)

    # Unknown / Randomized (Images "Unknown Vendor")
    # Ce sont des adresses privées générées aléatoirement
    "7A-EB-51": "Private Device (Randomized)", 
    "86-20-55": "Private Device (Randomized)",
}