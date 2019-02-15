# 复制window10壁纸、添加文件后缀、到当前目录
import os

# windows10壁纸路径
# 用户目录
user_home=os.getenv('USERPROFILE')
packages_home='AppData\\Local\\Packages'
# 我的壁纸位置 `Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy`
# 壁纸位置前缀
wallpaper_prefix = 'Microsoft.Windows.ContentDeliveryManager'

wallpaper_dir = 'LocalState\\Assets'

# 确定壁纸的目录
# sourceDir= 'C:\\Users\\Skiner\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'
dir1 = os.path.join(user_home,packages_home)
for file in os.listdir(dir1):
    if file.find(wallpaper_prefix) == 0:
        sourceDir = os.path.join(dir1,file,wallpaper_dir)
targerDir= './锁屏壁纸'

for file in os.listdir(sourceDir):
    # listdir放回的是文件名字符串
    sourceFile = os.path.join(sourceDir, file)
    targerFile = os.path.join(targerDir, file+".jpg")
    if os.path.isfile(sourceFile):
        if not os.path.exists(targerDir):
            os.makedirs(targerDir)
        # 过滤size 尺寸
        if os.path.getsize(sourceFile) > 1024 * 200:
            open(targerFile,'wb').write(open(sourceFile,'rb').read())
    if os.path.isdir(sourceFile):
        pass