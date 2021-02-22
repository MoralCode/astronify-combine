import ffmpeg
input_video = ffmpeg.input('input.gif')
input_audio = ffmpeg.input('input.wav')
input_audio2 = ffmpeg.input('clap.mp3')

merged_audio = ffmpeg.filter([input_audio, input_audio2], 'amix')

ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./output.mp4').run()