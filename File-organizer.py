import platform,os

image = ['.png','.jpg','jpeg']
video_type = ['.mov','mp4','mp3','.gif']
py_files = ['.py']
user = os.getlogin()
def python_files():
 path = input('Which directory do you want to clean?')
 path_to = input('Where would you like the specified files to be relocated? directory:')
 os.chdir(path)
 list = os.listdir()
 for file in list:
    if py_files[0] in file:
        try:
         os.system(f'mv {file} {path_to}')
         print('files moved!')
        except:
            print('There was an error!')
 if platform.system() == 'Windows':
    for file in list:
        if py_files[0] in file:
            try:
                os.system(f'move {file} {path_to}')
                print('Files moved!')
            except:
                print('There was an error!')
    
def images():
    path = input('Which directory do you want to clean?')
    path_to = input('Where would you like the specified files to be relocated? directory:')
    os.chdir(path)
    list = os.listdir()
    for file in list:
        if image[0] in file:
            print(file)
            try:
                os.system(f'mv {file} {path_to}')
                print('FIles moved!')
            except:
                print('There was an error!')
        elif image[1] in file:
            try:
                os.system(f'mv {file} {path_to}')
                print('Files Moved!')
            except:
                print('There was an error!')
        elif image[2] in file:
            try:
                os.system(f'mv {file} {path_to}')
                print('Files moved!')
            except:
                print('There was an error!')
        if platform.system() == 'Windows':
            for file in list:
              if image[0] in file:
                try:
                    os.system(f'move {file} {path_to}')
                    print('Files moved!')
                except:
                    print('There was an error!')
              elif image[1] in file:
                try:
                    os.system(f'move {file} {path_to}')
                    print('Files moved!')
                except:
                    print('There was an error!')
              elif image[2] in file:
                try:
                    os.system(f'move {file} {path_to}')
                    print('Files moved!')
                except:
                    print('There was an error!')

def videos():
    path = input('Which directory do you want to clean?')
    path_to = input('Where would you like the specified files to be relocated? directory:')
    os.chdir(path)
    list = os.listdir()
    for file in list:
        if video_type[0] in file:
            try:
                os.system(f'mv {file} {path_to}')
                print('Files moved!')
            except:
                print('There was an error!')
        elif video_type[1] in file:
            try:
                os.system(f'mv {file} {path_to}')
                print('Files moved!')
            except:
                print('There was an error!')
        elif video_type[2] in file:
            try:
                os.system(f'mv {file} {path_to}')
                print('Files moved!')
            except:
                print('There was an error!')
        elif video_type[3] in file:
            try:
                os.system(f'mv {file} {path_to}')
                print('Files moved!')
            except:
                print('There was an error!')
    if platform.system() == 'Windows':
        for file in list:
            if video_type[0] in file:
                try:
                    os.system(f'move {file} {path_to}')
                    print('Files moved!')
                except:
                    print('There was an error!')
            elif video_type[1] in file:
                try:
                    os.system(f'move {file} {path_to}')
                    print('Files moved!')
                except:
                    print('There was an error!')
            elif video_type[2] in file:
                try:
                    os.system(f'move {file} {path_to}')
                    print('Files moved!')
                except:
                    print('There was an error!')
            elif video_type[3] in file:
                try:
                    os.system(f'move {file} {path_to}')
                    print('Files moved!')
                except:
                    print('There was an error!')
            

def custom_extension():
    path = input('Which directory do you want to clean?')
    path_to = input('Where would you like the specified files to be relocated? directory:')
    ext = input('What is the file type? example(.txt):')
    os.chdir(path)
    list = os.listdir()
    for file in list:
        if ext in file:
            try:
                os.system(f'mv {file} {path_to}')
                print('Files moved!')
            except:
                print('There was an error!')
    if platform.system() =='Windows':
        for file in list:
            if ext in file:
                try:
                    os.system(f'move {file} {path_to}')
                    print('Files moved!')
                except:
                    print('There was an error!')

def main():
 art = '''
Hello {}! Please select an option!
[1] Move Images
[2] Move Videos
[3] Move Python Files
[4] Custom File Extensions
 '''.format(user)
 print(art)
 choice = input('/>')
 if choice == '1':
    images()
 elif choice == '2':
    videos()
 elif choice == '3':
   python_files()
 elif choice == '4':
    custom_extension()
main() 
