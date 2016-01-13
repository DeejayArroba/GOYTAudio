from pydub import AudioSegment
import pafy
import os
import shutil

current_dir = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(current_dir + "/dl"):
	os.makedirs(current_dir + "/dl")
if not os.path.exists(current_dir + "/output"):
	os.makedirs(current_dir + "/output")

csgo_dir = "/storage/SteamLibrary/steamapps/common/Counter-Strike Global Offensive/"

shutil.copyfile(current_dir + "/ytaudio.cfg", csgo_dir + "/csgo/cfg/ytaudio.cfg")

vid_url = input("Video url: ")
video = pafy.new(vid_url)

video.getbestaudio().download(filepath=current_dir+"/dl")

audio = AudioSegment.from_file(current_dir + "/dl/" + video.title + ".webm", "webm")
new_audio = audio.set_frame_rate(11025)
new_audio.export(current_dir + "/output/" + video.title + ".wav", format="wav")
os.remove(current_dir + "/dl/" + video.title + ".webm")

os.remove(csgo_dir + "/voice_input.wav")
shutil.move(current_dir + "/output/" + video.title + ".wav", csgo_dir + "/voice_input.wav")
