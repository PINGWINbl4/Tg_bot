import telebot
from telebot import types
import random
malvare = ['1.Здесь очень жарко или это из-за тебя?',
           '2.Ты словно Google или Яндекс. В тебе есть все, что я искал.',
           '3.Мне нужна карта и компас, чтобы не заблудиться в твоих глазах.',
           '4. Ты словно кофе: горячая, крепкая, вкусная, бодрящая и ароматная.',
           '5. Мне не нужен от тебя один секс. Мне нужны от тебя все твои сексы.',
           '6. С тобой можно в ресторан, в разведку и в ЗАГС.',
           '7. Я еще не выпил, но ты мне уже нравишься до умопомрачения.',
           '8. Красота спасет мир, а ты стоишь в самом первом ряду спасительниц.',
           '9. По шкале от 1 до 10, ты 100 баллов.',
           '10. Я принес тебе цветы, чтобы они увидели, что такое настоящая красота.',
           '11. К тебе даже пчелы клеятся.',
           '12. Твои родители, наверное, кулинары, раз у них вышла такая великолепная крошка.',
           '13. Ты прекрасная на 60%. К сожалению, остальные 40% тебя скрыты одеждой.',
           '14. Ты просто идеальна, но в тебе нужно поменять одно. Сменить фамилию на мою.',
           '15. Как тебе удается с каждым разом выглядеть все лучше и лучше?',
           '16. Платье на тебе тютелька в тютельку. Мне нравятся твои тютельки.',
           '17. Мое утро начинается не с кофе, а мысли о тебе.',
           '18. Спасибо за твою нежность, доброту и заботу.',
           '19. Ты потрясающая и клевая девчонка. Честно — честно.',
           '20. В средние века тебя бы сожгли на костре, из-за волшебной красоты.',
           '21. Ты невероятно красивая, словно греческая богиня из мифологии.',
           '22. Ты самая классная девушка в мире. 100%',
           '23. Твой отец был боксером? Своей внешностью ты посылаешь в нокаут любого.',
           '24. У тебя ангельское личико.',
           '25. У меня внезапно потемнело в глазах. От твоей красоты.',
           '26. Все, что мне нужно для счастья – это ты.',
           '27. Я постоянно думаю о тебе, а ты поселилась в моих мыслях.',
           '28. Ты не нуждаешься в косметике. Она нуждается в тебе.',
           '29. Ты мой любимый вид наркотиков',
           '30. Я не смотрю на твои потрясающие сиськи. Я смотрю на горячее сердце.',
           '31. Вместо Венеры Милосской должна быть твоя фигура.',
           '32. В мире всего есть три таких красотки: это ты, ты и еще раз ты.',
           '33. Я очень ценю и уважаю твое мнение.',
           '34. Думая о тебе, я начинаю улыбаться до ушей.',
           '35. Спасибо за поддержку и заботу, что ты оказываешь.',
           '36. Платье и аксессуары подходят к цвету твоих потрясающих глаз.',
           '37. Среди конкурса ангелов ты победила бы всех еще на кастинге.',
           '38. Твоя улыбка сводит меня с ума. Как у тебя получается так улыбаться?',
           '39. Я сделаю тебя по-настоящему счастливой.',
           '40. Твои родители воспитали отличную дочку. Золотая медаль.',
           '41. Ты потрясающая девушка. Ты должна это знаешь.',
           '42. Ради твоей улыбки хочется свернуть горы.',
           '43. Спасибо за то, что ты есть и такая замечательная.',
           '44. Ты определенно украшаешь этот мир и делаешь его лучше.',
           '45. Я очень скучаю по тебе.',
           '46. Мне кажется, что я в тебя влюбляюсь все сильнее и сильнее.',
           '47. Я никому тебя не отдам. Никому.',
           '48. Самое сложное с тобой – это прощаться.',
           '49. Твои уста сладкие и манящие, словно мед. А я «мохнатый пчол».',
           '50. Твои волосы и прическа восхитительны.',
           '51. У тебя ангельская и няшная внешность.',
           '52. Хочу быть только с тобой всю жизнь.',
           '53. Обожаю твою жизнерадостность и неиссякаемый позитив.',
           '54. Твои объятия нежные, словно я оказался в раю.',
           '55. Никогда не верил в любовь, до встречи с тобой.',
           '56. Вместе с тобой я чувствую себя живым.',
           '57. На тебя невозможно сердиться.',
           '58. У тебя очень заразительный смех. Словно колокольчики звенят.',
           '59. Ты всегда гармонично и безупречно выглядишь. Это природное?',
           '60. У тебя очень добрая, отзывчивая и нежная душа.',
           '61. Ты шикарно, отпадно и сногсшибательно выглядишь.',
           '62. Мне повезло, что судьба нас столкнула вместе.',
           '63. Ты мне больше, чем просто нравишься.',
           '64. Я бы сравнил тебя с цветком, но такого красивого не существует.',
           '65. Ты делаешь меня самым счастливым человеком на свете.',
           '66. Надеюсь, что наши дети будут похожи на тебя.',
           '67. Хочу заботиться о тебе и оберегать от всего мира.',
           '68. Ты девушка моей мечты. Или мечта моей жизни.',
           '69. От твоего внешнего вида у меня, иногда, перехватывает дыхание.',
           '70. Ты моя единственная.',
           '71. Ты родственная и самая близкая мне душа.',
           '72. В толпе людей подсознательно пытаюсь найти тебя.',
           '73. Когда ты улыбаешься, то словно солнце выходит из-за туч.',
           '74. Куда ты спрятала крылья и нимб? Ты определено ангел.',
           '75. Ты понимаешь меня без слов. С одного взгляда и мысли.',
           '76. Ты по-настоящему прикольная девчонка.',
           '77. Звуки твоего голоса заставляют мое сердце биться быстрее.',
           '78. Ты самый важный человек для меня на всем целом свете.',
           '79. Твоя фигура очень стройная, словно тростинка.',
           '80. Ты словно счастливый талисман, который приносит удачу и радость.',
           '81. Хочу, чтобы время останавливалось, когда мы рядом.',
           '82. Твой голос очень очаровательный и мелодичный. Как у волшебницы.',
           '83. Ты сумасшедшая и непостижимая девушка. Таких уже не выпускают.',
           '84. Красотка – это твое прозвище в детстве и второе имя.',
           '85. Идеальных людей не бывает. Но ты ведь есть.',
           '86. Во времена Трои, война была бы из-за тебя.',
           '87. Ты очень экстравагантная и необычная девушка.',
           '88. Ты из тех роковых красоток, в которых влюбляются без памяти.',
           '89. У тебя скромный и одновременно сильный характер.',
           '90. Ты волшебная и изумительная девушка, словно из сказки.',
           '91. Ты очень женственная и красивая. Само воплощение женственности.',
           '92. С тобой я становлюсь лучшей версией самого себя.',
           '93. Ты украсила мою жизнь и сделала ее яркой.',
           '94. У тебя очень нежная и приятная кожа',
           '95. Ты само совершенство, от улыбки до жестов выше всяких похвал.',
           '96. Ты не только мое солнце и луна, но и целая вселенная.',
           '97. Мне очень хорошо с тобой.',
           '98. У тебя очень милое и нежное лицо, когда ты спишь.',
           '99. У тебя выразительный, ясный, проницательный и умный взгляд.',
           '100. Мое сердце трепещет при встрече с тобой.',
           '101. Ты словно принцесса, которая вдохновляет на подвиги.',
           '102. В твоих глазах можно утонуть.',
           '103. Твой голос заставляет меня влюбляться раз за разом.',
           '104. В тебе кроется бесшабашная девчонка, которая потрясает меня.',
           '105. Твои движения, слова и внешность всегда меня заводят.',
           '106. У тебя прекрасное чувство юмора.',
           '108. У тебя отличная кожа.',
           '109. Твой румянец на щечках очень милый.',
           '110. Платье сидит на тебе идеально и восхитительно.',
           '111. Ты очень целеустремленная и волевая девушка.',
           '112. Мне кажется, что ты умеешь читать мои мысли.',
           '113. Ты очень хорошая хозяйка.',
           '115. У тебя шаловливый и непосредственно детский характер.',
           '116. О тебе я думаю утром, когда просыпаюсь. С мыслями о тебе ложусь спать.',
           '117. В тебе живет мечтательница и чуткая душа. Это редкость.',
           '119. Ты очень стильная и умеешь подбирать гардероб.',
           '120. У тебя прекрасный и необычный цвет глаз.',
           '121. Ты неповторимая и уникальная.',
           '122. Люблю разговоры с тобой.',
           '123. У меня отнялась речь, когда я тебя увидел. Отлично выглядишь.',
           '124. Ты бесценная и неповторимая девушка.',
           '125. После нашей встречи я начал верить в судьбу.',
           '126. Ты привлекательна даже тогда, когда злишься.',
           '127. Твои манеры отличны и даже безупречны.',
           '128. Ты замечательная напарница по любому делу.',
           '129. Ты словно глоток воздуха в морской бездне.',
           '130. У тебя прелестные, пушистые и длинные реснички.',
           '131. Ты выглядишь как ТОП – модель с обложки.',
           '132. Не могу представить жизнь без тебя.',
           '133. Мне нравится в тебе внешностью, характер, темперамент. Абсолютно все.',
           '134. Ты очень горячая и сексуальная девушка.',
           '135. У тебя очень много талантов и достоинств. Природа постаралась.',
           '136. Ты так отлично и сексуально выглядишь, что это почти неприлично.',
           '137. Твои ножки очень красивые и горячие.',
           '138. У тебя незабываемые глаза и взгляд, которые запоминаешь на всю жизнь.',
           '139. Твой голос и внешность опьяняют.',
           '140. У тебя ослепительная и подкупающая улыбка.',
           '141. Своим характером ты способна установить мир на земле.',
           '142. Ты умеешь завораживать и очаровывать.',
           '143. У тебя очень мудрый и рассудительный ум. Откуда это?',
           '144. Ты отлично двигаешься, гибкая и очень пластична.',
           '145. В тебе скрывается опасная секс-бомба.',
           '146. Ты похожа на произведение искусства. Неповторима и бесценна.',
           '147. В тебе естественная женственность и очарование.',
           '148. Моя душа искала твою целую вечность.',
           '149. Ты поменяла мою жизнь к лучшему. Это много стоит.',
           '150. Ты очень утонченная, чуткая и ранимая натура.']

bot = telebot.TeleBot('1909043549:AAEcA5_OG_KLJcoPQBjNR31kokCRsH0qgLg')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    love_botton = types.KeyboardButton('Показать насколько я люблю тебя<3')

    markup.add(love_botton)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}.Дорогая Саша, сегодня 3 месяца с момента того, как мы познакомились. Мне не хватит и всех слов мира, чтобы описать насоклько сильно я люблю тебя, но тут я подобрал несколько.'.format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def welcome_text(message):
    if message.chat.type == 'private':
        if message.text == 'start':
            bot.send_message(message.chat.id, '')
        if message.text == 'Показать насколько я люблю тебя<3':
            bot.send_message(message.chat.id, malvare[random.randint(0, len(malvare)-1)])
try: bot.polling(non_stop=True, interval=1)
except(ConnectionAbortedError, ConnectionError, ConnectionResetError, ConnectionRefusedError): bot.polling(non_stop=True, interval=1), welcome_text

