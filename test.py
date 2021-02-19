import ffmpeg
input_video = ffmpeg.input('input.gif')
input_audio = ffmpeg.input('input.mp3')


ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./output.mp4').run()