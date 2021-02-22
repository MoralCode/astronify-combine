import ffmpeg

BPM = 60
# 60 BPM is one beat per second, or 1 Hz
hertz=BPM/60
tick_sound = ffmpeg.input(tick_filename)
actual_tick_duration = float(tick_sound.probe()['streams'][0]['duration'])

padding_needed_per_tick = hertz - actual_tick_duration
input_video = ffmpeg.input('input.gif')
input_audio = ffmpeg.input('input.wav')
input_audio2 = ffmpeg.input('clap.mp3')
input_audio3 = ffmpeg.input('clapfast.mp3')

claps = ffmpeg.filter([input_audio2, input_audio3], 'amix')

merged_audio = ffmpeg.filter([input_audio, claps], 'amix')

ffmpeg.concat(
	input_video,
	merged_audio,
	v=1,
	a=1
).output('testout.mp4').run()