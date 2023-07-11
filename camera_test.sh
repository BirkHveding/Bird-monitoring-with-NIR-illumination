#!/bin/bash
light='NIR_close_plate' # is the lamp on?
dist='0.6m' # distance from camera to bird
velocity='NO' # NO or YES

# 60 fps
now=$(date +"%H%M%S")
libcamera-vid -t 5000 --shutter 3000000 --gain 16 --framerate 60 -o fps60_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
mv fps60* Documents/Skarv_exp/fps60

now=$(date +"%H%M%S")
libcamera-vid -t 5000 --gain 16 --framerate 60 -o fps60_shutter0s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
mv fps60* Documents/Skarv_exp/fps60

now=$(date +"%H%M%S")
libcamera-vid -t 5000 --framerate 60 -o fps60_shutter0s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
mv fps60* Documents/Skarv_exp/fps60

# 50 fps
now=$(date +"%H%M%S")
libcamera-vid -t 5000 --shutter 3000000 --gain 16 --framerate 50 -o fps50_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
mv fps50* Documents/Skarv_exp/fps50

# 40 fps
now=$(date +"%H%M%S")
libcamera-vid -t 8000 --shutter 3000000 --gain 16 --framerate 40 -o fps40_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
mv fps40* Documents/Skarv_exp/fps40

now=$(date +"%H%M%S")
libcamera-vid -t 5000 --gain 16 --framerate 40 -o fps40_shutter0s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
mv fps40* Documents/Skarv_exp/fps40

now=$(date +"%H%M%S")
libcamera-vid -t 5000 --framerate 40 -o fps40_shutter0s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
mv fps40* Documents/Skarv_exp/fps40

# # 30 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 8000 --shutter 3000000 --gain 16 --framerate 30 -o fps30_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps30* Documents/Skarv_exp/fps30

# # 20 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 8000 --shutter 3000000 --gain 16 --framerate 20 -o fps20_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps20* Documents/Skarv_exp/fps20

# # 10 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 8000 --shutter 3000000 --gain 16 --framerate 10 -o fps10_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps10* Documents/Skarv_exp/fps10

# # 5 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 5000 --shutter 3000000 --gain 16 --framerate 5 -o fps5_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps5* Documents/Skarv_exp/fps5

# # 2 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 10000 --shutter 3000000 --gain 16 --framerate 2 -o fps2_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps2* Documents/Skarv_exp/fps2

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000 --shutter 3000000 --framerate 2 -o fps2_shutter3s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps2* Documents/Skarv_exp/fps2

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000 --gain 16 --framerate 2 -o fps2_shutter0s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps2* Documents/Skarv_exp/fps2

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000 --framerate 2 -o fps2_shutter0s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps2* Documents/Skarv_exp/fps2

# # 1 fps
# now=$(date +"%H%M%S")
# libcamera-vid -t 10000 --shutter 3000000 --gain 16 --framerate 1 -o fps1_shutter3s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps1* Documents/Skarv_exp/fps1

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000 --shutter 3000000 --framerate 1 -o fps1_shutter3s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps1* Documents/Skarv_exp/fps1

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000 --gain 16 --framerate 1 -o fps1_shutter0s_gain16_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %-n
# mv fps1* Documents/Skarv_exp/fps1

# now=$(date +"%H%M%S")
# libcamera-vid -t 10000 --framerate 1 -o fps1_shutter0s_gain0_time${now}_dist${dist}_light${light}_vel${velocity}.h264 %%-n
# mv fps1* Documents/Skarv_exp/fps1
