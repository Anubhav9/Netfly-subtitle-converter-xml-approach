import json
from lxml import etree
import boto3
import math

subtitle_xml=etree.parse("subtitles.xml")
root=subtitle_xml.getroot()
ns = {'tt': 'http://www.w3.org/ns/ttml'}
"""
JSON Structure is {"start_time":x_seconds,"end_time":y_seconds,"translated_text":text}
"""

all_subtitles=root.xpath("//tt:p",namespaces=ns)
len_all_subtitles=len(all_subtitles)
print(len_all_subtitles)
subtitles_json=[]
for i in range(1,len_all_subtitles+1):
    print(f"We are at subtitle number::{i}")
    subtitle_number="subtitle"+str(i)
    start_time=root.xpath(f"//tt:p[@xml:id='{subtitle_number}']/@begin",namespaces=ns)
    start_time=start_time[0].replace("t","")
    start_time=int(start_time)
    start_time=start_time/10000000
    end_time=root.xpath(f"//tt:p[@xml:id='{subtitle_number}']/@end",namespaces=ns)
    end_time=end_time[0].replace("t","")
    end_time=int(end_time)
    end_time=end_time/10000000
    base_text_message=root.xpath(f"//tt:p[@xml:id='{subtitle_number}']//text()",namespaces=ns)
    final_text=""
    for j in range(0,len(base_text_message)):
        final_text=final_text+base_text_message[j].replace("\n","").replace("\t","")
    print(f"Final Text Message is::{final_text}")
    aws_translate_client=boto3.client("translate",region_name="ap-northeast-1")
    try:
        translated_text=aws_translate_client.translate_text(Text=final_text,SourceLanguageCode="ja",TargetLanguageCode="en")
        translated_text=translated_text["TranslatedText"]
        temp_json={"start_time":math.floor(start_time),"end_time":math.floor(end_time),"translated_text":translated_text}
        subtitles_json.append(temp_json)

    except Exception as e:
        print(f"Error in translating text::{final_text}")
        print(f"Printing Exception::{e}")

subtitles_json=json.dumps(subtitles_json)
print(subtitles_json)
