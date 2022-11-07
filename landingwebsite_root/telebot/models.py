"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                                                                   ""   
""   · To connect a tg bot, you need to find BotFather account in the telegram and write him a command '/newbot'     ""   
""                                                                                                                   ""   
""   · Then you will receive a link to a bot and to an API key                                                       ""   
""                                                                                                                   ""   
""   · To get a chat_id, you need to create a new group and add a bot there. Then you need to copy the numbers from  ""   
""     the address bar with the symbol '-'. ( The link will be like https://web.telegram.org/z/#-123456789. You need "" 
""     only -123456789. That is your chat_id. Attention, you must open the telegram in your browser)                 ""  
""                                                                                                                   ""   
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from django.db import models


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат айди')
    tg_message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
