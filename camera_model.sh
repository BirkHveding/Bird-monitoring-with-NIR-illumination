#!/bin/bash
light='NIR_40mA' # is the lamp on?
dist='0.5m' # distance from camera to bird
velocity='NO' # NO or YES
color='black_white_ROOMwScreen_rounded'

# 120 fps
now=$(date +"%H%M%S")
libcamera-vid -t 5000  --level 4.2 --shutter 3000000 --gain 16 --framerate 120 -o fps60color${color}_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n

# 60 fps
now=$(date +"%H%M%S")
libcamera-vid -t 5000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --gain 16 --framerate 60 -o fps60color${color}_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps60* Documents/Box_exp/fps60

# now=$(date +"%H%M%S")
# libcamera-vid -t 5000  --level 4.2 --widht 1920 --height 1080 --gain 16 --framerate 60 -o fps60color${color}_shutter0s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps60* Documents/Box_exp/fps60

# now=$(date +"%H%M%S")
# libcamera-vid -t 5000  --level 4.2 --widht 1920 --height 1080 --framerate 60 -o fps60color${color}_shutter0s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps60* Documents/Box_exp/fps60

# # 50 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 5000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --gain 16 --framerate 50 -o fps50color${color}_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps50* Documents/Box_exp/fps50

# # 40 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 8000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --gain 16 --framerate 40 -o fps40color${color}_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps40* Documents/Box_exp/fps40

# now=$(date +"%H%M%S")
# libcamera-vid -t 5000  --level 4.2 --widht 1920 --height 1080 --gain 16 --framerate 40 -o fps40color${color}_shutter0s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps40* Documents/Box_exp/fps40

# now=$(date +"%H%M%S")
# libcamera-vid -t 5000  --level 4.2 --widht 1920 --height 1080 --framerate 40 -o fps40color${color}_shutter0s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps40* Documents/Box_exp/fps40

# # 30 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 8000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --gain 16 --framerate 30 -o fps30color${color}_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps30* Documents/Box_exp/fps30


# # 20 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 8000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --gain 16 --framerate 20 -o fps20color${color}_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps20* Documents/Box_exp/fps20

# # 10 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 8000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --gain 16 --framerate 10 -o fps10color${color}_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps10* Documents/Box_exp/fps10

# # 5 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 5000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --gain 16 --framerate 5 -o fps5_color${color}shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps5* Documents/Box_exp/fps5

# now=$(date +"%H%M%S")
# libcamera-vid -t 5000  --level 4.2 --widht 1920 --height 1080 --gain 16 --framerate 5 -o fps5_color${color}shutter0s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps5* Documents/Box_exp/fps5

# # 2 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 10000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --gain 16 --framerate 2 -o fps2_color${color}shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps2* Documents/Box_exp/fps2

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --framerate 2 -o fps2_color${color}shutter3s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps2* Documents/Box_exp/fps2

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000  --level 4.2 --widht 1920 --height 1080 --gain 16 --framerate 2 -o fps2_color${color}shutter0s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps2* Documents/Box_exp/fps2

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000  --level 4.2 --widht 1920 --height 1080 --framerate 2 -o fps2_color${color}shutter0s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps2* Documents/Box_exp/fps2

# # 1 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 10000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --gain 16 --framerate 1 -o fps1_color${color}shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps1* Documents/Box_exp/fps1

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000  --level 4.2 --widht 1920 --height 1080 --shutter 3000000 --framerate 1 -o fps1_color${color}shutter3s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps1* Documents/Box_exp/fps1

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000  --level 4.2 --widht 1920 --height 1080 --gain 16 --framerate 1 -o fps1_color${color}shutter0s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps1* Documents/Box_exp/fps1

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000  --level 4.2 --widht 1920 --height 1080 --framerate 1 -o fps1_color${color}shutter0s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 -n
# mv fps1* Documents/Box_exp/fps1
