from pathlib import Path
from PIL import Image
import time
import shutil
import threading

jpg_quality = 95

src_folder_root = str(Path("./src_images/").resolve())
dst_folder_root = str(Path("./dst_images/").resolve())
print(src_folder_root)

p = Path("./src_images")
# 再帰的にフォルダとファイルのリストを作る
all_list = (list(p.glob("**/*")))
total_num = len(all_list)
rest_num = total_num
print("got list total: " + str(total_num))


start = time.time()

for itemPath in all_list:
    p = Path(itemPath)
    src_abs_path = str(p.resolve())
    dst_abs_path = dst_folder_root + src_abs_path.replace(src_folder_root,'')

    if(p.exists() and p.is_dir()):
        Path(dst_abs_path).mkdir(parents=True, exist_ok=True)
    elif(p.exists() and p.is_dir() != True):
        if(p.suffix == '.png'):
            # 既存ファイルを readモードで読み込み
            input_im = Image.open(src_abs_path)
            rgb_im = input_im.convert('RGB')
            rgb_im.save(dst_abs_path[:-3] + "jpg",quality=jpg_quality)

        else:
            shutil.copyfile(src_abs_path,dst_abs_path)    
    rest_num -= 1

    #1秒ごとに進捗報告
    elapsed_time = time.time() - start
    if(elapsed_time >= 1):
        start = time.time()
        percent = 100 -  (rest_num / total_num * 100)
        print("\r\nprocess:" + str(rest_num) + '/' + str(total_num) + " / percent:"+str(round(percent, 1)) + "%" )
        print("now:" + src_abs_path)   