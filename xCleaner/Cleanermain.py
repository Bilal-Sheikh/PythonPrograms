import os
import shutil

def AlreadyExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def MoveFiles(files, foldername):
    for file in files:
        shutil.move(file, foldername)

files = os.listdir()
files.remove("Cleanermain.py")

AlreadyExists("Docs")
AlreadyExists("Images")
AlreadyExists("Videos")
AlreadyExists("Audio")
AlreadyExists("Compressed")
AlreadyExists("Executable")
AlreadyExists("Others")
# print(files)

DocsExt = [".pdf", ".txt", ".docx", ".doc"]
moveToDocs = [docs for docs in files if docs.lower().endswith(tuple(DocsExt))]
# print(moveToDocs)

ImageExt = [".jpg", ".jpeg", ".gif", ".png", ".ai", ".bmp", ".ico", ".ps", ".psd", ".svg", ".tif", ".tiff"]
moveToImages = [images for images in files if images.lower().endswith(tuple(ImageExt))]
# print(moveToImages)

VideoExt = [".mp4", ".mkv", ".flv", ".mov", ".webm", ".avi", ".m4v", ".mpg", ".mpeg", "wvm"]
moveToVideos = [videos for videos in files if videos.lower().endswith(tuple(VideoExt))]
# print(moveToVideos)

AudioExt = [".aif", ".cda", ".midi", ".mid", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"]
moveToAudio = [audios for audios in files if audios.lower().endswith(tuple(AudioExt))]
# print(moveToAudios)

CompressedExt = [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".z", ".zip"]
moveToCompressed = [compressed for compressed in files if compressed.lower().endswith(tuple(CompressedExt))]
# print(moveToCompressed)

ExecutableExt = [".apk", ".bat", ".bin", ".cgi", ".pl", ".exe", ".com", ".jar", ".msi", ".py", ".wsf"]
moveToExecutable = [exe for exe in files if exe.lower().endswith(tuple(ExecutableExt))]
# print(moveToExecutable)

OtherExt = []
for other in files:
    moveToOthers = os.path.splitext(other)[1].lower()
    if (moveToOthers not in DocsExt) and (moveToOthers not in ImageExt
    ) and (moveToOthers not in VideoExt) and (moveToOthers not in AudioExt
    ) and (moveToOthers not in CompressedExt) and (moveToOthers not in ExecutableExt
    ) and os.path.isfile(other):
        OtherExt.append(other)
# print(OtherExt)

MoveFiles(moveToDocs, "Docs")
MoveFiles(moveToImages, "Images")
MoveFiles(moveToVideos, "Videos")
MoveFiles(moveToAudio, "Audio")
MoveFiles(moveToCompressed, "Compressed")
MoveFiles(moveToExecutable, "Executable")
MoveFiles(OtherExt, "Others")