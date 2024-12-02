# def cor_serv(masg_mail):
#     ra=['.com','.ru','.net']
#     zz=False
#     for i in ra:
#         if masg_mail[len(masg_mail)-len(i):len(masg_mail)+1]==i:
#            zz=True
#            break
#     return zz
# def send_email(message, recipient,*, sender="university.help@gmail.com"):
#     if sender == recipient:
#         print("Нельзя отправить письмо самому себе!")
#     elif '@' not in sender or '@' not in recipient or cor_serv(recipient)!=True or cor_serv(sender)!=True :
#         print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
#     elif sender == "university.help@gmail.com":
#         print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
#     else:
#         print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
#
#
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.ruteacher@mail.uk')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
def cor_serv(masg_mail):
    ra=['.com','.ru','.net']
    zz=False
    for i in ra:
        if masg_mail[len(masg_mail)-len(i):len(masg_mail)+1]==i:
           zz=True
           break
    return zz
def send_email(message, recipient,*, sender="university.help@gmail.com"):
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif '@' not in sender or '@' not in recipient or cor_serv(recipient)!=True or cor_serv(sender)!=True :
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.ruteacher@mail.uk')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')