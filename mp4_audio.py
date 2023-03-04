from moviepy.video.io.VideoFileClip import VideoFileClip

# укажите путь к видео файлу
video_path = input('Укажите путь к видео файлу: ')

# загружаем видео файл
video = VideoFileClip(video_path)

# извлекаем аудио из видео
audio = video.audio

# сохраняем аудио в файл
name_audio = input('укажите имя аудио: ')

audio_path = f"../../Музыка/{name_audio}.mp3"

audio.write_audiofile(audio_path)

# освобождаем ресурсы
video.reader.close()
video.audio.reader.close_proc()
