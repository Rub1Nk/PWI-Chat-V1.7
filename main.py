# импорт переменных
from config import verify, sp, maxnick, maxmsg, portt, systemnickname, heading, ownernick, ownernick2, ownernick3, ownernick4, ban_list, version, update_info, update_date, help_info_adm, help_info, fr_ch, user_list
from admin import anickpass, onickpass

# импорт библиотек
import time
import os
import datetime
from colorama import Fore, Style

# создание директории для логов
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# функция записи логов
log_filename = f"ChatHistory_{datetime.datetime.now().strftime('%Y.%m.%d_%H-%M-%S')}.txt"
log_path = os.path.join(log_dir, log_filename)
def log_print(*args, **kwargs):
    with open(log_path, "a") as f:
        print(*args, **kwargs, file=f)
    print(*args, **kwargs)

os.system('cls||clear')

# вывод информации
log_print('• [&] Chat:', Fore.GREEN + 'Online', Style.RESET_ALL)
dt_now = str(datetime.datetime.now())
log_print(f'\n[&] Время запуска по серверу:\n{dt_now[:10]} • {dt_now[:19][11:]}\n')
log_print(f'[&] Owner Password - {onickpass}\n[&] Admin Password - {anickpass}')
log_print('\nLogs:\n')

# анти-краш система
def main():
  try:
      pass
  except Exception as e:
      log_print(f"Произошла ошибка: {e}")
      print("Перезапуск программы...")
      os.execv(sys.executable, ['python'] + sys.argv)

# импорт основы
import asyncio

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js

# параметры
chat_msgs = []
online_users = set()

MAX_MESSAGES_COUNT = 250

current_datetime = datetime.datetime.now()

# блок с чатом и панелью
async def main():
    global chat_msgs
  
    put_markdown(heading)

    msg_box = output()
    put_scrollable(msg_box, height=300, keep_bottom=True)

    # отправка приветсвенного сообщения
    msg_box.append(put_markdown(f'`{systemnickname}` Для подключения в чату - введите свой никнейм!'))

    # запрос никнейма
    online_users.add(ownernick)
    online_users.add(ownernick2)
    online_users.add(ownernick3)
    online_users.add(ownernick4)
    
    nickname = await input('🌐 Вход',required=True, placeholder=f'Придумайте ник (макс.симв: {maxnick})', validate=lambda n: 'Этот никнейм уже занят!' if n in online_users or n == '📢' else None)
  
    # вход в админку
    if nickname in ban_list:
      dt_now = str(datetime.datetime.now())
      if nickname == nickname:
        toast('Данный никнейм находится в чёрном списке!')
        run_js('window.location.reload()')
        log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [!] Заблокированный пользователь {nickname} пытался присоеденится к чату')
      
    elif nickname == anickpass:
        nickname = await input('👔 Никнейм для админ аккаунта',required=True, placeholder='Придумайте никнейм')
        nickname = nickname + verify
        online_users.add(nickname)
        user_list.append(nickname)
        toast('Вы вошли в аккаунт администратора!')
        chat_msgs.append(('`👔 Админ`', f' `{nickname}` подключился!'))
        msg_box.append(put_markdown(f'`👔 Админ` `{nickname}` подключился!'))
        msg_box.append(put_markdown('• Для получения информации и помощи - отправьте команду `/help`\n• Так же ознакомьтесь с правилами отправив команду `/rules`'))
        
        dt_now = str(datetime.datetime.now())
        log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [!] Вход в админ аккаунт', nickname)
  
    # вход в создателя
    elif nickname == onickpass:
        nickname = await input('👑 Никнейм для аккаунта создателя:',required=True, placeholder='Придумайте никнейм')
        nickname = nickname + verify
        online_users.add(nickname)
        user_list.append(nickname)
        toast('Вы вошли в аккаунт создателя!')
        chat_msgs.append(('`👑 Создатель`', f' `{nickname}` подключился!'))
        msg_box.append(put_markdown(f'`👑 Создатель` `{nickname}` подключился!'))
        msg_box.append(put_markdown('• Для получения информации и помощи - отправьте команду `/help`\n• Так же ознакомьтесь с правилами отправив команду `/rules`'))

        dt_now = str(datetime.datetime.now())
        log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [!] Вход в аккаунт создателя', nickname)
      
    # проверка ника
    else:
        dt_now = str(datetime.datetime.now())
        if '  ' in nickname:
            print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [~] Недопуск! Ник содержит 2 пробела! (Nick: {nickname})')
            run_js('window.location.reload()')
        elif nickname == ' ':
            print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [~] Недопуск! Ник состоит из пробела!')
            run_js('window.location.reload()')
        elif ' ' in nickname:
            print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [~] Недопуск! Ник содержит невидимый символ! (Nick: {nickname})')
            run_js('window.location.reload()')
        elif 'RubiNk' in nickname:
            print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [~] Недопуск! Ник содержит невидимый символ! (Nick: {nickname})')
            run_js('window.location.reload()')
        elif '✓' in nickname:
            print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [~] Недопуск! Ник содержит галочку! (Nick: {nickname})')
            run_js('window.location.reload()')
        else:
            # подключение к чату
            nickname = nickname[:maxnick]
            online_users.add(nickname)
            user_list.append(nickname)
            chat_msgs.append(('📢', f'Пользователь `{nickname}` подключился!'))
            msg_box.append(put_markdown(f'📢 Пользователь `{nickname}` подключился!'))
            msg_box.append(put_markdown('• Для получения информации и помощи - отправьте команду `/help`\n• Так же ознакомьтесь с правилами отправив команду `/rules`'))
           
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [' + Fore.GREEN + '•' + Style.RESET_ALL + ']', nickname, '- Connected')
            
    refresh_task = run_async(refresh_msg(nickname, msg_box))

    # блок для отправки сообщений
    while True:
        data = await input_group('💭 Новое сообщение', [
            input(placeholder=f'Текст сообщения... (макс.симв: {maxmsg})', name='msg', autocomplete="off", required=False),
            actions(name='cmd', buttons=['📨 Отправить сообщение', {'label': '🚪 Выйти', 'type': 'cancel'}])
        ], validate=lambda m: ('msg', 'Введите текст сообщения!') if m['cmd'] == '📨 Отправить сообщение' and not m["msg"] else None)

      
        if data is None:
            break

        # команды
        elif nickname in ban_list:
          dt_now = str(datetime.datetime.now())
          toast('Вы были заблокированы!')
          run_js('window.location.reload()')

        elif data['msg'] == '/help':
          dt_now = str(datetime.datetime.now())
          log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [/]', nickname, 'вызвал команду /help')
          if verify in nickname:
            msg_box.append(put_markdown(f'\n{help_info_adm}'))
          else:
            msg_box.append(put_markdown(f'\n{help_info}'))

        elif data['msg'] == '/rules':
          dt_now = str(datetime.datetime.now())
          log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [/]', nickname, 'вызвал команду /rules')
          msg_box.append(put_markdown(f'\n`📕 Правила`:\n`1.` Нет спаму / флуду\n`2.` Нет рекламе / самопиару\n`3.` Нет оскорблениям / срачам\n\n– В прочем правил больше нету. Главное не пересекайте черту и ведите себя адекватно.`\n'))

        elif data['msg'] == '/updates':
          log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [/]', nickname, 'вызвал команду /updates')
          dt_now = str(datetime.datetime.now())
          msg_box.append(put_markdown(f'\n📰 Последнее обновление: `{version}`\n{update_info}\nОбновлено: `{update_date}`'))
                                 
        elif data['msg'] == '/time':
          log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [/]', nickname, 'вызвал команду /time')
          dt_now = str(datetime.datetime.now())
          msg_box.append(put_markdown(f'\n⌚ Информация с сервера:\n`~ {dt_now[:10]}\n• {dt_now[:19][11:]}`'))

        elif data['msg'] == '/ban':
          dt_now = str(datetime.datetime.now())
          if verify in nickname:
            ban_user = await input('Введите никнейм который необходимо занести в ЧС',required=True, placeholder='Ник')
            if ban_user in user_list:
              ban_list.append(ban_user)
              online_users.remove(ban_user)
              user_list.remove(ban_user)
              chat_msgs.append(('🚫', f'Пользователь `{ban_user}` был заблокирован!'))
              toast(f'{ban_user} был добавлен в ЧС!')
              log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [&]', nickname, 'забанил', ban_user)
            else:
              toast('Такого пользователя нету онлайн!')
          else:
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [×]', nickname, 'пытался вызвать команду /ban')
            toast('Недостаточно прав!')

        elif data['msg'] == '/unban':
          dt_now = str(datetime.datetime.now())
          if verify in nickname:  
            unban_user = await input('Введите никнейм который необходимо убрать из ЧС',required=True, placeholder='Ник')
            if unban_user in ban_list:
              ban_list.remove(unban_user)
              chat_msgs.append(('✅', f'Пользователь `{unban_user}` был разбанен!'))
              toast(f'{unban_user} был убран из ЧС!')
              log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [&]', nickname, 'разбанил', unban_user)
            else:
              toast('Такого пользователя нету в бан-списке!')
          else:
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [×]', nickname, 'пытался вызвать команду /unban')
            toast('Недостаточно прав!')

        elif data['msg'] == '/kick':
          dt_now = str(datetime.datetime.now())
          if verify in nickname:
            kick_user = await input('Введите никнейм который необходимо убрать из онлайна',required=True, placeholder='Ник')
            if kick_user in user_list:
              online_users.remove(kick_user)
              user_list.remove(kick_user)
              toast(f'{kick_user} был кикнут!')
              log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [&]', nickname, 'кикнул', kick_user)
            else:
              toast('Такого пользователя нету онлайн!')
          else:
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [×]', nickname, 'пытался вызвать команду /ban')
            toast('Недостаточно прав!')

        elif data['msg'] == '/list':
          dt_now = str(datetime.datetime.now())
          if verify in nickname:
            user_counts = len(user_list)
            msg_box.append(put_markdown(f'\n🌐 Сейчас онлайн: `{user_counts}`'))
            msg_box.append(put_markdown('\n'.join(map(str, user_list))))
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [&]', nickname, 'вызвал команду /list')
          else:
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [×]', nickname, 'пытался вызвать команду /list')
            toast('Недостаточно прав!')
      
        elif data['msg'] == '/ban_list':
          dt_now = str(datetime.datetime.now())
          if verify in nickname:
            ban_counts = len(ban_list)
            msg_box.append(put_markdown(f'\n🚫 Заблокированных пользователей: `{ban_counts}`'))
            msg_box.append(put_markdown('\n'.join(map(str, ban_list))))
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [&]', nickname, 'вызвал команду /ban_list')
          else:
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [×]', nickname, 'пытался вызвать команду /ban_users')
            toast('Недостаточно прав!')
      
        elif '/toast ' in data['msg']:
          if verify in nickname:
            tmsg = data['msg'].replace('/toast ', '')
            toast(tmsg)
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [Toast]', nickname + ': ' + tmsg)
          else:
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [×]', nickname, 'пытался вызвать команду /toast')
            toast('Недостаточно прав!')
            
        elif data['msg'] == '/fmsg':
          dt_now = str(datetime.datetime.now())
          if verify in nickname:
            fknick = await input('Ник',required=True, placeholder='Ник')
            fkmsg = await input('Сообщение', placeholder='Текст')
            chat_msgs.append((fknick, fkmsg))
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [' + nickname + ']', '[Fake]', fknick + ': ' + fkmsg)
          else:
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [×]', nickname, 'пытался вызвать команду /fmsg')
            toast('Недостаточно прав!')
            
        elif data['msg'] == '/fcdmsg':
          if verify in nickname:
            fkcdnick = await input('Ник',required=True, placeholder='Ник')
            cdq = await input('Ответ:',required=True, placeholder='c - подкл | d - откл')
            if cdq == 'c':
              chat_msgs.append(('📢', f'Пользователь `{nickname}` подключился!'))
              dt_now = str(datetime.datetime.now())
              log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [Fake]', nickname, '[' + Fore.GREEN + '•' + Style.RESET_ALL + ']', fkcdnick, '- Connected')
            elif cdq == 'd':
              chat_msgs.append(('🔌', f'Пользователь `{fkcdnick}` отключился!'))
              dt_now = str(datetime.datetime.now())
              log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [Fake]', nickname, '[' + Fore.RED + '•' + Style.RESET_ALL + ']', fkcdnick, '- Disconnected')
          else:
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [×]', nickname, 'пытался вызвать команду /fcdmsg')
            toast('Недостаточно прав!')

        # проверка на пробелы в сообщении
        elif data['msg'] == ' ':
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [~] Пустое сообщение пользователя', nickname, 'не было отправлено (является пробелом)')
        elif '  ' in data['msg']:
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [~] Пустое сообщение пользователя', nickname, 'не было отправлено (содержит 2 пробела)')
        elif '  ' in data['msg']:
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [~] Пустое сообщение пользователя', nickname, 'не было отправлено (содержит невидимый символ)')
        else:
            msg_box.append(put_markdown(f'`{nickname}`: {data["msg"][:maxmsg]}'))
            chat_msgs.append((nickname, data['msg'][:maxmsg]))
            dt_now = str(datetime.datetime.now())
            log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}]', nickname + ': ' + data['msg'][:maxmsg])
  
    refresh_task.close()

    # отключение от чата
    online_users.remove(nickname)
    user_list.remove(nickname)
    toast('Вы отключились из чата!')
    msg_box.append(put_markdown(f'🔌 Пользователь `{nickname}` отключился!'))
    chat_msgs.append(('🔌', f'Пользователь `{nickname}` отключился!'))
    dt_now = str(datetime.datetime.now())
    log_print(f'[{dt_now[:10]} • {dt_now[:19][11:]}] [' + Fore.RED + '•' + Style.RESET_ALL + ']', nickname, '- Disconnected')

    put_buttons(['🔁 Перезайти'], onclick=lambda btn:run_js('window.location.reload()'))

# прочее
async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs)

    while True:
        await asyncio.sleep(1)
        
        for m in chat_msgs[last_idx:]:
            if m[0] != nickname:
                msg_box.append(put_markdown(f'`{m[0]}`: {m[1]}'))
        
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]
        
        last_idx = len(chat_msgs)

if __name__ == '__main__':
    start_server(main, debug=True, port=portt, cdn=False)
    main()