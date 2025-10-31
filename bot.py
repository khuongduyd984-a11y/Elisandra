import nextcord
impost os
from nextcord.ext import commands

# ─────────────────────────────
#  Cấu hình cơ bản
# ─────────────────────────────
intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ─────────────────────────────
#  Câu hỏi kiểm tra
# ─────────────────────────────
question = "Thủ đô của Việt Nam là gì?"
answer = "hà nội"
role_name = "học sinh"  # tên role trong server

# ─────────────────────────────
#  Khi bot khởi động
# ─────────────────────────────
@bot.event
async def on_ready():
    print(f" Bot đã đăng nhập thành công dưới tên: {bot.user}")

# ─────────────────────────────
#  Khi có người mới vào server
# ─────────────────────────────
@bot.event
async def on_member_join(member):
    try:
        await member.send(
            f"Chào {member.name}! Trả lời đúng câu hỏi sau để vào server:\n {question}"
        )
    except:
        print(f"Không thể gửi DM cho {member.name} (có thể họ chặn DM)")

# ─────────────────────────────
# 💬 Khi bot nhận tin nhắn DM
# ─────────────────────────────
@bot.event
async def on_message(message):
    if message.guild is None and not message.author.bot:  # nếu là DM riêng
        if message.content.lower().strip() == answer:
            guild = bot.guilds[0]  # nếu bot chỉ có trong 1 server
            role = nextcord.utils.get(guild.roles, name=role_name)
            member = guild.get_member(message.author.id)

            if role and member:
                await member.add_roles(role)
                await message.channel.send(" Chính xác! Bạn đã được cấp quyền truy cập server.")
            else:
                await message.channel.send(" Không tìm thấy role hoặc thành viên trong server.")
        else:
            await message.channel.send("Sai rồi  thử lại nhé.")

    await bot.process_commands(message)

# ─────────────────────────────
#  Lệnh test nhanh
# ─────────────────────────────
@bot.command()
async def test(ctx):
    await ctx.send(f" Bot đang hoạt động tốt, {ctx.author.mention}!")

# ─────────────────────────────
# 🔑 Token bot
# ─────────────────────────────

bot.run(os.getenv("DISCORD_TOKEN"))
