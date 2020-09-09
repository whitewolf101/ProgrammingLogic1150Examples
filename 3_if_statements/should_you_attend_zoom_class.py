"""
When this class is online, everyone is
always welcome in our zoom sessions!

However if
  - You have watched the videos
  - written the lecture video code and everything worked
  - you feel like you understand all the materials
  - you've done the lab
  - you've turned in your lab
  - you don't have any questions

You don't need to attend.

"""
have_watched_lecture_videos = True
written_lecture_video_code = True
all_lecture_video_code_worked = True
understand_materials = True
done_lab = False
turned_in_lab = False
have_questions = True

if have_questions == True:
    print('please ask questions!')
else:
    print('Great! Let me know if any questions come up in the future!')

if have_watched_lecture_videos and written_lecture_video_code and all_lecture_video_code_worked and understand_materials and done_lab and turned_in_lab and not have_questions:
    print('Great! you dont need to attend the zoom. but you are welcome!')
else:
    print('Please come to zoom and we\'ll answer questions and work on lab')

