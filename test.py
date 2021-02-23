import ffmpeg
from shutil import copyfile
from pydub import AudioSegment

BPM = 60

def bpm_to_time_per_tick(bpm):
	return (1/bpm)/60
 

def calculate_padding_needed_ms(target_sec, actual_sec):
	return int((target_sec - actual_sec)*1000)


def process_tick(bpm, filename):
	tick = AudioSegment.from_wav(filename)
	pad = calculate_padding_needed_ms(bpm_to_time_per_tick(bpm), tick.duration_seconds)
	padding = AudioSegment.silent(duration=pad)
	final_tick = tick + padding
	final_tick.export(filename, format="wav")

tick_filename='oneclap-megasqueeze'
# make a copy of the source tick noise so it doesnt get overwritten
#TODO: check if a file with the same name exists so as to prevent creating a new one
newname = tick_filename + "." + str(BPM) + ".wav"
copyfile(tick_filename +".wav", newname)

process_tick(BPM, newname)

input_video = ffmpeg.input('input.gif')
input_audio = ffmpeg.input('input.wav')
ticks = ffmpeg.input(newname, stream_loop=-1)

#merge the input audio with a forever-looping tempo at the provided frequency
merged_audio = ffmpeg.filter([input_audio, ticks], 'amix', duration="shortest")

ffmpeg.concat(
	input_video,
	merged_audio,
	v=1,
	a=1
).output('testout.mp4').run()