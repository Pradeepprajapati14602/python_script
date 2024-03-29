# import json

# # Replace 'Hathway.json' with the correct JSON file path
# json_file_path = 'all_ocr_results.json'

# # Open the JSON file for reading
# with open(json_file_path, 'r') as json_file:
#     data = json.load(json_file)

# # Define your condition-checking function
# def satisfies_condition(text):
#     setup_boxes = [
#                     {"name": "airtelXstream_mum_MH", "type": "channel_no", "conditions": [{"coordinates": coor.generate(828,138,121,46), "text": "regex: options|optlons"}]},
#                     {"name": "denOld_MUM&denOld_BR", "type": "channel_name", "conditions": [{"coordinates": coor.generate(592, 281, 160, 70), "text": "info"}]},
                    
#                     # {"name": "den_MUM&den_MH&den_DL&den_GJ&den_UP", "type": "channel_name", "conditions": [{"coordinates": coor.generate(640, 240, 160, 40), "text": "regex: othergenres|oothergenres"}, {"coordinates": coor.generate(1060, 250, 150, 80), "text": "regex: den|\w{1,3}"}]},
#                     # {"name": "hathway_MUM&hathway_MH&hathway_DL&hathway_RJ&hathway_AP&hathway_MP", "type": "channel_name", "conditions": [{"coordinates": coor.generate(640, 240, 160, 40), "text": "regex: othergenres|oothergenres"}, {"coordinates": coor.generate(1060, 250, 150, 80), "text": "regex: @|hath"}]},

#                     {"name": "den_mum_MH&hathway_mum_MH&hathway_MH&hathway_DL&hathway_RJ&hathway_AP&hathway_MP&den_MH&den_DL&den_GJ&den_UP&den_HR&hathway_HR&den_JH&hathway_sikkim_NESA&hathway_OD", "type": "channel_name", "conditions": [{"coordinates": coor.generate(600, 240, 400, 50), "text": "regex: (othergenres|oothergenres|addfav|deletefav)"}, {"coordinates": coor.generate(860, 100, 300, 60), "text": "regex: (^\w{3}(.|,)\d{1,2}\w{2,3}\d{6}:\d{2}[ap][m]$)|(\d{2}:\d{2}[ap][m])"}]},
#                     {"name": "tataskyBinge_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(182,235,105, 50),"text": "regex: dhome&home"},{"coordinates": coor.generate(520,226,195,71), "text": "regex: ^(?:[A-Za-z]{2}&miniguide)"},{"coordinates": coor.generate(300,240,190,30),"text": "regex: [/*]&Options"}]},
#                     {"name": "jpr_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(924,124,233,43),"text": "regex: (\d{2}/\d{4}:\d{2})&(\d{2}/\d{2})&(d{2}:\d{2})"}]},
#                     {"name": "jpr_mum_MH&netVision_UP", "type": "channel_name", "conditions": [{"coordinates": coor.generate(970,105,120,40),"text": "regex: ^\d{2}:\d{2}[ap][m]$"}]},
#                     {"name": "dishtv_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(873,55,278,109),"text": "regex: vcno"}]},

#                     {"name": "hathway_old_mum_MH&hathway_old_MH", "type": "channel_no", "conditions": [{"coordinates": coor.generate(100, 290, 200, 30),"text": "regex: ^(?:[A-Za-z]+,)?([A-Za-z]+)(\d{1,2})$"}, {"coordinates": coor.generate(75, 225, 60, 40),"text": "regex: ^\d+"}]},

#                     {"name": "airtel_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(69, 253, 346, 55),"text": "regex: (\d{2}:\d{2})"}]},

#                     {"name": "suntv_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(698, 255, 235, 65),"text": "addtofav"}]},
#                     {"name": "tatasky_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(833, 246, 169, 57),"text": "alerts"}]},
#                     {"name": "tatasky_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(850, 243, 169, 57),"text": "alerts"}]},
#                     {"name": "freedish_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(174, 277, 212, 48),"text": "regex: \d{4}/\d{2}/\d{2}"}]},
                    
#                     {"name": "inCable_PCMC_MH&bhimaRiddhi_MH","type": "channel_no", "conditions": [{"coordinates": coor.generate(750, 140, 1500, 40), "text": "regex: stereo"}, {"coordinates": coor.generate(900, 140, 300, 40),"text": "regex: (^\d{2}/\d{2}/\d{4})"}]},

#                     {"name": "digiCable_MH","type": "channel_name", "conditions": [{"coordinates": coor.generate(260, 770, 150, 100),"text": "regex: jpr&jp2"}, {"coordinates": coor.generate(1450, 700, 200, 50),"text": "regex: ^\d{2}:\d{2}[ap][m]$"}]},
#                     {"name": "icc_pune_MH","type": "channel_name", "conditions": [{"coordinates": coor.generate(1045, 200, 200, 40),"text": "regex: ^\d{2}:\d{4}\/(\d{1}|\d{2})\/\d{2}$"}, {"coordinates": coor.generate(250, 200, 70, 40),"text": "regex: ^\d+"}]},

#                     {"name": "inCable_mum_MH&gtpl_jaipur_RJ&gtpl_vizag_AP&digiana_MP&gtpl_dibrugarh_NESA&gtpl_tripura_NESA&gtplGlobelChapter_NESA&nxt_modernComm_NESA","type": "channel_name", "conditions": [{"coordinates": coor.generate(690,190,500,150),"text": "regex: (^\d{1,3}\/\d{2})|(^\d{2}\/\d{4}[:;]\d{2})|allchannel"},{"coordinates": coor.generate(200,310,600,40),"text": "regex: schedule|channelinfo|mail"},]},

#                     # {"name": "inCable_GJ", "type": "channel_no", "conditions": [{"coordinates": coor.generate(675, 300, 60, 40),"text": "mail"}, {"coordinates": coor.generate(465, 300, 150, 60),"text": "regex: ^channelinfo"}]}, NEED TO UPDATE

#                     {"name": "7Star_mum_MH","type": "channel_name", "conditions": [{"coordinates": coor.generate(1065, 165, 90, 30),"text": "regex: ^\d{2}:\d{2}"}]},
#                     # {"name": "signet_mum_MH","type": "channel_name", "conditions": [{"coordinates": coor.generate(140, 170, 160, 40),"text": "signet"}, {"coordinates": coor.generate(990, 110, 200, 30),"text": "regex: ^\d{2}:\d{2}[ap][m]$"}]},

#                     {"name": "gtplHomeCable_MH&gtpl_GJ&gtpl_MP&gtpl_BR", "type": "channel_name", "conditions": [{"coordinates": coor.generate(85, 280, 180, 40),"text": "regex: \d{2}:\d{2}\w{3}\d{2}(,|.)\d{4}"}]},

#                     {"name": "rajeshMulti_MH","type": "channel_no", "conditions": [{"coordinates": coor.generate(1095, 270, 150, 40),"text": "regex: (rajes&rajesh)"}]},
#                     {"name": "gtplsss_mum_MH","type": "channel_no", "conditions": [{"coordinates": coor.generate(835, 200, 100, 40),"text": "servinfo"}, {"coordinates": coor.generate(705, 250, 250, 70),"text": "regex: (\w{3}\d{1,2}\w{3}[|\/]?\d{2}:\d{2})|(\d{2}:\d{2})"}]},
#                     {"name": "videoconD2H_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(75, 270, 180, 60),"text": "regex: ^\w{2,10}[,.]?\d{1,2}\w{2,3}$"},
#                                                                                           {"coordinates": coor.generate(150, 235, 90, 60),"text": "regex: \d{2}:\d{2}"}]},
#                         # {"coordinates": coor.generate(885, 60, 300, 100),"text": "regex: .*?(\d{11}).*?"}, 
                        
#                     {"name": "jpr_sbbv_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(935,125,235,40),"text": "regex: (\d{2}/\d{4}:\d{2})&(\d{2}/\d{2})&(d{2}:\d{2})"}]},
#                     {"name": "metroCast_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(940, 140, 250, 40),"text": "regex: ^\d{2}\/\d{4}:\d{2}"}, {"coordinates": coor.generate(935, 230, 235, 50),"text": "metr()cast"}]},

#                     {"name": "signet_mum_MH&smc_sangli_MH&scc_pune_MH&ddc_DL&netset_GJ&digiCable_RJ&infotech_jhunjhun_RJ&digiCable_agra_UP&royalCable_MP&kristalCity_khandawa_MP&jpr_MH&netVision_UP&grandVision_CH&impact_manipur_NESA", "type": "channel_name", "conditions": [{"coordinates": coor.generate(950, 80, 200, 100),"text": "regex: ^\d{2}:\d{2}[ap][m]$"}]},

#                    ]

#     return 'specific_keyword' in text

# # Iterate through the data and check if each text value satisfies the condition
# for key, value in data.items():
#     if satisfies_condition(value):
#         print(f"The text '{value}' satisfies the condition for key '{key}'")
#     else:
#         print(f"The text '{value}' does not satisfy the condition for key '{key}'")





import json
import re
import coordinates as coor
# import coordinates

# Replace 'Hathway.json' with the correct JSON file path
json_file_path = 'all_ocr_results.json'

# Open the JSON file for reading
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Define your setup_boxes list
setup_boxes = [{"name": "airtelXstream_mum_MH", "type": "channel_no", "conditions": [{"coordinates": coor.generate(828,138,121,46), "text": "regex: options|optlons"}]},
                    {"name": "denOld_MUM&denOld_BR", "type": "channel_name", "conditions": [{"coordinates": coor.generate(592, 281, 160, 70), "text": "info"}]},
                    
                    # {"name": "den_MUM&den_MH&den_DL&den_GJ&den_UP", "type": "channel_name", "conditions": [{"coordinates": coor.generate(640, 240, 160, 40), "text": "regex: othergenres|oothergenres"}, {"coordinates": coor.generate(1060, 250, 150, 80), "text": "regex: den|\w{1,3}"}]},
                    # {"name": "hathway_MUM&hathway_MH&hathway_DL&hathway_RJ&hathway_AP&hathway_MP", "type": "channel_name", "conditions": [{"coordinates": coor.generate(640, 240, 160, 40), "text": "regex: othergenres|oothergenres"}, {"coordinates": coor.generate(1060, 250, 150, 80), "text": "regex: @|hath"}]},

                    {"name": "den_mum_MH&hathway_mum_MH&hathway_MH&hathway_DL&hathway_RJ&hathway_AP&hathway_MP&den_MH&den_DL&den_GJ&den_UP&den_HR&hathway_HR&den_JH&hathway_sikkim_NESA&hathway_OD", "type": "channel_name", "conditions": [{"coordinates": coor.generate(600, 240, 400, 50), "text": "regex: (othergenres|oothergenres|addfav|deletefav)"}, {"coordinates": coor.generate(860, 100, 300, 60), "text": "regex: (^\w{3}(.|,)\d{1,2}\w{2,3}\d{6}:\d{2}[ap][m]$)|(\d{2}:\d{2}[ap][m])"}]},
                    {"name": "tataskyBinge_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(182,235,105, 50),"text": "regex: dhome&home"},{"coordinates": coor.generate(520,226,195,71), "text": "regex: ^(?:[A-Za-z]{2}&miniguide)"},{"coordinates": coor.generate(300,240,190,30),"text": "regex: [/*]&Options"}]},
                    {"name": "jpr_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(924,124,233,43),"text": "regex: (\d{2}/\d{4}:\d{2})&(\d{2}/\d{2})&(d{2}:\d{2})"}]},
                    {"name": "jpr_mum_MH&netVision_UP", "type": "channel_name", "conditions": [{"coordinates": coor.generate(970,105,120,40),"text": "regex: ^\d{2}:\d{2}[ap][m]$"}]},
                    {"name": "dishtv_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(873,55,278,109),"text": "regex: vcno"}]},

                    {"name": "hathway_old_mum_MH&hathway_old_MH", "type": "channel_no", "conditions": [{"coordinates": coor.generate(100, 290, 200, 30),"text": "regex: ^(?:[A-Za-z]+,)?([A-Za-z]+)(\d{1,2})$"}, {"coordinates": coor.generate(75, 225, 60, 40),"text": "regex: ^\d+"}]},

                    {"name": "airtel_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(69, 253, 346, 55),"text": "regex: (\d{2}:\d{2})"}]},

                    {"name": "suntv_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(698, 255, 235, 65),"text": "addtofav"}]},
                    {"name": "tatasky_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(833, 246, 169, 57),"text": "alerts"}]},
                    {"name": "tatasky_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(850, 243, 169, 57),"text": "alerts"}]},
                    {"name": "freedish_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(174, 277, 212, 48),"text": "regex: \d{4}/\d{2}/\d{2}"}]},
                    
                    {"name": "inCable_PCMC_MH&bhimaRiddhi_MH","type": "channel_no", "conditions": [{"coordinates": coor.generate(750, 140, 1500, 40), "text": "regex: stereo"}, {"coordinates": coor.generate(900, 140, 300, 40),"text": "regex: (^\d{2}/\d{2}/\d{4})"}]},

                    {"name": "digiCable_MH","type": "channel_name", "conditions": [{"coordinates": coor.generate(260, 770, 150, 100),"text": "regex: jpr&jp2"}, {"coordinates": coor.generate(1450, 700, 200, 50),"text": "regex: ^\d{2}:\d{2}[ap][m]$"}]},
                    {"name": "icc_pune_MH","type": "channel_name", "conditions": [{"coordinates": coor.generate(1045, 200, 200, 40),"text": "regex: ^\d{2}:\d{4}\/(\d{1}|\d{2})\/\d{2}$"}, {"coordinates": coor.generate(250, 200, 70, 40),"text": "regex: ^\d+"}]},

                    {"name": "inCable_mum_MH&gtpl_jaipur_RJ&gtpl_vizag_AP&digiana_MP&gtpl_dibrugarh_NESA&gtpl_tripura_NESA&gtplGlobelChapter_NESA&nxt_modernComm_NESA","type": "channel_name", "conditions": [{"coordinates": coor.generate(690,190,500,150),"text": "regex: (^\d{1,3}\/\d{2})|(^\d{2}\/\d{4}[:;]\d{2})|allchannel"},{"coordinates": coor.generate(200,310,600,40),"text": "regex: schedule|channelinfo|mail"},]},

                    # {"name": "inCable_GJ", "type": "channel_no", "conditions": [{"coordinates": coor.generate(675, 300, 60, 40),"text": "mail"}, {"coordinates": coor.generate(465, 300, 150, 60),"text": "regex: ^channelinfo"}]}, NEED TO UPDATE

                    {"name": "7Star_mum_MH","type": "channel_name", "conditions": [{"coordinates": coor.generate(1065, 165, 90, 30),"text": "regex: ^\d{2}:\d{2}"}]},
                    # {"name": "signet_mum_MH","type": "channel_name", "conditions": [{"coordinates": coor.generate(140, 170, 160, 40),"text": "signet"}, {"coordinates": coor.generate(990, 110, 200, 30),"text": "regex: ^\d{2}:\d{2}[ap][m]$"}]},

                    {"name": "gtplHomeCable_MH&gtpl_GJ&gtpl_MP&gtpl_BR", "type": "channel_name", "conditions": [{"coordinates": coor.generate(85, 280, 180, 40),"text": "regex: \d{2}:\d{2}\w{3}\d{2}(,|.)\d{4}"}]},

                    {"name": "rajeshMulti_MH","type": "channel_no", "conditions": [{"coordinates": coor.generate(1095, 270, 150, 40),"text": "regex: (rajes&rajesh)"}]},
                    {"name": "gtplsss_mum_MH","type": "channel_no", "conditions": [{"coordinates": coor.generate(835, 200, 100, 40),"text": "servinfo"}, {"coordinates": coor.generate(705, 250, 250, 70),"text": "regex: (\w{3}\d{1,2}\w{3}[|\/]?\d{2}:\d{2})|(\d{2}:\d{2})"}]},
                    {"name": "videoconD2H_mum_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(75, 270, 180, 60),"text": "regex: ^\w{2,10}[,.]?\d{1,2}\w{2,3}$"},
                                                                                          {"coordinates": coor.generate(150, 235, 90, 60),"text": "regex: \d{2}:\d{2}"}]},
                        # {"coordinates": coor.generate(885, 60, 300, 100),"text": "regex: .*?(\d{11}).*?"}, 
                        
                    {"name": "jpr_sbbv_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(935,125,235,40),"text": "regex: (\d{2}/\d{4}:\d{2})&(\d{2}/\d{2})&(d{2}:\d{2})"}]},
                    {"name": "metroCast_MH", "type": "channel_name", "conditions": [{"coordinates": coor.generate(940, 140, 250, 40),"text": "regex: ^\d{2}\/\d{4}:\d{2}"}, {"coordinates": coor.generate(935, 230, 235, 50),"text": "metr()cast"}]},

                    {"name": "signet_mum_MH&smc_sangli_MH&scc_pune_MH&ddc_DL&netset_GJ&digiCable_RJ&infotech_jhunjhun_RJ&digiCable_agra_UP&royalCable_MP&kristalCity_khandawa_MP&jpr_MH&netVision_UP&grandVision_CH&impact_manipur_NESA", "type": "channel_name", "conditions": [{"coordinates": coor.generate(950, 80, 200, 100),"text": "regex: ^\d{2}:\d{2}[ap][m]$"}]},


]

# Define a function to check if conditions are satisfied
def check_conditions(text, conditions):
    
    for condition in conditions:
        condition_text = condition["text"]
        # Check if the condition is satisfied
        if "regex:" in condition_text:
            regex_pattern = condition_text.replace("regex:", "")
            if re.search(regex_pattern, text):
                return True
        elif text == condition_text:
            return True
    return False

# Iterate through the data and check if each text value satisfies the conditions
for key, value in data.items():
    for box in setup_boxes:
        if box["name"] == key:
            if check_conditions(value, box["conditions"]):
                print(f"The text '{value}' satisfies the conditions for box '{box['name']}'")
