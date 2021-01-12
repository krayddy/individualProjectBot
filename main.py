# This Python file uses the following encoding: utf-8

import telebot
from telebot import types


bot = telebot.TeleBot("1284427462:AAHPyWAvdRGT104ol7fCp4PXELJmAi55EwU", parse_mode="Markdown")

#region variables

#region keyboards
main_menu_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
main_menu_keyboard.add('Unity', 'Blender', 'РУПД', 'Загрузка документов')

download_menu_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
download_menu_keyboard.add('РУПД', 'Unity', 'Blender', 'Назад')

unity_menu_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
unity_menu_keyboard.add('Вспомним предыдущие шаги', 'Установка Unity', 'Регистрация', 'Установка Unity Editor',
                        'Установка Vuforia и добавление в Unity', 'Сборка проекта', 'Решение задачи', 'Назад')

blender_menu_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
blender_menu_keyboard.add('Почему', 'Что такое Blender', 'Скачивание и установка Blender', 'Создание файла',
                          'Основы работы с Blender',
                          'Создание пирамиды с сечением и подготовка к экспорту в Unity', 'Назад')

rupd_menu_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_keyboard.add('Пояснительная записка', 'Результаты освоения дисциплины',
                       'Содержание учебного предмета', 'Тематическое планирование с указанием количества часов',
                       'Оценка индивидуального проекта', 'Учебно-методическое обеспечение дисциплины', 'Назад')

rupd_menu_block2_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block2_keyboard.add('Метапредметные результаты', 'Предметные результаты', 'Назад', 'В главное меню')

rupd_menu_block2_block1_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block2_block1_keyboard.add('Регулятивные универсальные учебные действия',
                                     'Познавательные универсальные учебные действия',
                                     'Коммуникативные универсальные учебные действия', 'Назад', 'В главное меню')

rupd_menu_block2_block2_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block2_block2_keyboard.add('Обучаемый получит представление', 'Обучаемый сможет',
                                     'Обучаемый научится', 'Назад', 'В главное меню')

rupd_menu_block3_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block3_keyboard.add('Часть 1. Основы проектной деятельности',
                              'Часть 2. Выполнение обучаемым индивидуального проекта', 'Назад', 'В главное меню')

rupd_menu_block3_block1_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block3_block1_keyboard.add('Тема 1. Введение в проектную культуру', 'Тема 2. Инициализация проекта',
                                     'Тема 3. Базовое проектирование и исследование',
                                     'Тема 4. Информационные ресурсы проектной и исследовательской деятельности',
                                     'Тема 5. Презентация результатов проектной деятельности',
                                     'Тема 6. Защита результатов проектной и исследовательской деятельности',
                                     'Тема 7. Коммуникативные навыки',
                                     'Тема 8. Рефлексия проекта. Индивидуальный прогресс', 'Назад', 'В главное меню')

rupd_menu_block5_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block5_keyboard.add('Оценка метапредметных результатов обучения по уровню '
                              'сформированности Универсальных Учебных Действий (УУД)',
                              'Оценка сформированности ключевых компетенций учащихся, '
                              'которые относятся к общему (метапредметному) содержанию образования',
                              'Оценка сформированности ключевых компетенций учащихся «4к»', 'Назад', 'В главное меню')

rupd_menu_block5_block1_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block5_block1_keyboard.add('Требования, устанавленные ФГОС к результатам образования '
                                     '(ФГОС ООО, п.II.8, ФГОС СОО, п.II.6)',
                                     'Метапредметные результаты включают освоенные обучающимися',
                                     'Основные особенности оценки личностных, метапредметных и предметных '
                                     'результатов обучения',
                                     'Особенности индивидуального проекта',
                                     'Материалы, которые должны быть представлены к защите итогового проекта',
                                     'Организация защиты проекта',
                                     'Процедура оценивания сформированности УУД при защите реализованного проекта',
                                     'Критерии оценивания итогового проекта',
                                     'Подходы к оцениванию результатов итогового процесса',
                                     'Уровни сформированности навыков проектной деятельности (интегральный подход)',
                                     'Назад', 'В главное меню')

rupd_menu_block5_block2_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block5_block2_keyboard.add('Компетентность отличается', 'Три уровня компетенций', 'Ключевые компетенции',
                                     'Уровни компетенций и способы деятельности учащихся', 'Назад', 'В главное меню')

rupd_menu_block5_block3_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block5_block3_keyboard.add('К 2020 году каждый востребованный сотрудник должен будет уметь',
                                     'Система “4К”', 'Подробнее о каждом из четырех «К»',
                                     'Оценка прогресса в критическом мышлении, креативности, коммуникации и кооперации',
                                     'Назад', 'В главное меню')
#endregion

#region block_messages
main_menu_message = "Содержание:\n" \
                    "1. Unity\n" \
                    "2. Blender\n" \
                    "3. РУПД\n" \
                    "4. Загрузка документов"
download_menu_message = "Содержание:\n" \
                        "1. РУПД\n" \
                        "2. Unity\n" \
                        "3. Blender"
unity_menu_message = "Содержание:\n" \
                     "1. Вспомним предыдущие шаги\n" \
                     "2. Установка Unity\n" \
                     "3. Регистрация\n" \
                     "4. Установка Unity Editor\n" \
                     "5. Установка Vuforia и добавление в Unity\n" \
                     "6. Сборка проекта\n" \
                     "7. Решение задачи\n"
blender_menu_message = "Содержание:\n" \
                       "1. Почему\n" \
                       "2. Что такое Blender\n" \
                       "3. Скачивание и установка Blender\n" \
                       "4. Создание файла\n" \
                       "5. Основы работы с Blender\n" \
                       "6. Создание пирамиды с сечением и подготовка к экспорту в Unity\n"
rupd_main_menu_message = "Содержание:\n" \
                         "1. Пояснительная записка\n" \
                         "2. Результаты освоения дисциплины\n" \
                         "3. Содержание учебного предмета\n" \
                         "4. Тематическое планирование с указанием количества часов\n" \
                         "5. Оценка индивидуального проекта\n" \
                         "6. Учебно-методическое обеспечение дисциплины"
rupd_menu_block2_message = "Содержание:\n" \
                           "1. Метапредметные результаты\n" \
                           "2. Предметные результаты"
rupd_menu_block2_block1_message = "Содержание:\n" \
                                  "1. Регулятивные универсальные учебные действия\n" \
                                  "2. Познавательные универсальные учебные действия\n" \
                                  "3. Коммуникативные универсальные учебные действия"
rupd_menu_block2_block2_message = "Содержание:\n" \
                                  "1. Обучаемый получит представление\n" \
                                  "2. Обучаемый сможет\n" \
                                  "3. Обучаемый научится"
rupd_menu_block3_message = "Содержание:\n" \
                           "1. Часть 1. Основы проектной деятельности\n" \
                           "2. Часть 2. Выполнение обучаемым индивидуального проекта с применением " \
                           "AR-технологии-проекта «оживление учебника» в виде простого AR-приложения " \
                           "для Android-устройства с помощью ПО Blender, Unity3D и Vuforia"
rupd_menu_block3_block1_message = "Содержание:\n" \
                                  "1. Введение в проектную культуру\n" \
                                  "2. Инициализация проекта\n" \
                                  "3. Базовое проектирование и исследование\n" \
                                  "4. Информационные ресурсы проектной и исследовательской деятельности\n" \
                                  "5. Презентация результатов проектной деятельности\n" \
                                  "6. Защита результатов проектной и исследовательской деятельности\n" \
                                  "7. Коммуникативные навыки\n" \
                                  "8. Рефлексия проекта. Индивидуальный прогресс"
rupd_menu_block5_message = "Содержание:\n" \
                           "1. Оценка метапредметных результатов обучения по уровню сформированности Универсальных Учебных Действий (УУД)\n" \
                           "2. Оценка сформированности ключевых компетенций учащихся, которые относятся к общему (метапредметному) содержанию образования\n" \
                           "3. Оценка сформированности ключевых компетенций учащихся «4к»"
rupd_menu_block5_block1_message = "Содержание:\n" \
                                  "1. Требования, устанавленные ФГОС к результатам образования " \
                                  "(ФГОС ООО, п.II.8, ФГОС СОО, п.II.6)\n" \
                                  "2. Метапредметные результаты включают освоенные обучающимися\n" \
                                  "3. Основные особенности оценки личностных, метапредметных и предметных " \
                                  "результатов обучения\n" \
                                  "4. Особенности индивидуального проекта\n" \
                                  "5. Материалы, которые должны быть представлены к защите итогового проекта\n" \
                                  "6. Организация защиты проекта\n" \
                                  "7. Процедура оценивания сформированности УУД при защите реализованного проекта\n" \
                                  "8. Критерии оценивания итогового проекта\n" \
                                  "9. Подходы к оцениванию результатов итогового процесса\n" \
                                  "10. Уровни сформированности навыков проектной деятельности (интегральный подход)"
rupd_menu_block5_block2_message = "Содержание:\n" \
                                  "1. Компетентность отличается\n" \
                                  "2. Три уровня компетенций\n" \
                                  "3. Ключевые компетенции\n" \
                                  "4. Уровни компетенций и способы деятельности учащихся"
rupd_menu_block5_block3_message = "Содержание:\n" \
                                  "1. К 2020 году каждый востребованный сотрудник должен будет уметь\n" \
                                  "2. Система “4К”\n" \
                                  "3. Подробнее о каждом из четырех «К»\n" \
                                  "4. Оценка прогресса в критическом мышлении, креативности, коммуникации и кооперации"
rupd_menu_block6_message = "[1.Индивидуальный проект. 10-11 классы: учебное пособие для общеобразовательных " \
                           "организаций / М. В. Половкова, А. В. Носов, Т. В. Половкова, М. В. Майсак. - " \
                           "Москва: Просвещение, 2019. - 159 с.](https://www.labirint.ru/books/649611/) \n\n" \
                           "[2.Индивидуальный проект: рабочая тетрадь. 10-11 классы. Учебное пособие/Л.Е.Спиридонова," \
                           " Б.А. Комаров,О.В.Маркова,В.М.Стацунова. – СПб.КАРО, 2019. – 104с.]" \
                           "(https://cutt.ly/bgnU3d7)\n\n" \
                           "[3.Компетентностный подход в обучении: учебно-методическое пособие / авт.-сост." \
                           " О.В. Еремкина, Н.Б. Федорова, Д.В. Морин, М.А. Борисова; Ряз. гос. ун-т им. " \
                           "С.А. Есенина. – Рязань, 2010 – 48 с.]" \
                           "(https://www.rsu.edu.ru/wp-content/uploads/2015/11/Kompetentnostny-podhod-v-obuchenii.pdf)\n\n" \
                           "[4. Компетенции “4К”: формирование и оценка на уроке: Практические рекомендации" \
                           "/ авт.-сост. М. А. Пинская, А. М. Михайлова. – 76с.]" \
                           "(https://publications.hse.ru/mirror/pubs/share/direct/345295660.pdf)\n\n" \
                           "[5.Проектная и исследовательская деятельность школьников в контексте требований ФГОС" \
                           "/Материалы Л.И.Асановой, к.п.н., доцента ГБОУ ДПО " \
                           "«Нижегородский институт развития образования».]" \
                           "(https://rosuchebnik.ru/upload/iblock/733/733b6b3d76aab4abae1ff92989545fbf.pdf)"
#endregion

#region unity_text
unity = (
[
    'До этого при работе в Blender, вы уже создали 3D модель пирамиды, которую разделили на 3 части: сечение, верхняя часть пирамиды, нижняя часть пирамиды и сохранили себе на компьютер в формате .obj. Напомним, что, в качестве примера, мы рассматриваем стереометрическую задачу. Для дальнейших преобразований пирамиды обратимся к платформе разработки Unity 3D вместе с библиотекой Vuforia.'
],

[
    'Для начала работы с Unity перейдите на [официальный сайт](https://unity.com) и нажмите кнопку Get started ',
    'После перехода на новую страницу выберите вкладку Individual и далее, нажмите на кнопку Get Started ',
    'После перехода на новую страницу выберите StartHere на вкладке First-Time Users. После нажатия данной кнопки начнется скачивание установщика UnityHub – специального установщика для продуктов Unity. В нем необходимо выбрать папку, в которую вы хотите в дальнейшем установить UnityHub и сам Unity. \nПосле завершения откройте UnityHub. Для дальнейшей установки Unity понадобится UnityID. Регистрацию можно совершить либо на официальном сайте, либо в приложении, следуя подсказкам.'
],

[
    'Зайдите на [официальный сайт Unity](https://unity.com) и нажмите на иконку профиля в правом верхнем углу, после чего нажмите кнопку Create a unity ID ',
    'После этого вы автоматически переместитесь на страницу создания профиля. На ней необходимо ввести свой E-mail, Пароль, Имя, Фамилию и Username. Все данные вводятся на латинице.\nПосле введения своих данных отметьте первые две галочки и пройдите проверку на робота(Re-Captcha). Далее нажимаем на кнопку Create a Unity ID',
    'Пример введённых данных',
    'Далее вам будет необходимо подтвердить ваш E-mail',
    'Для этого необходимо найти на указанной вами почте письмо от Unity, в котором будет ссылка на подтверждение E-mail. После перехода по ссылке ваш аккаунт будет создан и подтвержден, и вы сможете начать работать с Unity.\nПри выборе лицензии Unity выбирайте индивидуальную бесплатную.'
],

[
    'В открытом UnityHub выберите вкладку Installs и далее нажмите на кнопку Add ',
    'Вам будет предложено несколько версий Unity. Советуем установить версию, которую рекомендует сам UnityHub. Нажмите на кнопку Next ',
    'Далее будут представлены несколько модулей на установку. Так какнаше AR-приложение будет на IOS/Android - выбирайте данные модули ',
    'После завершения установки UnityEditor кликните на вкладку Projects, затем на кнопку New',
    'Откроется Окно создания проекта. Выберите опцию 3D и нажмите кнопку Create.'
],

[
    'Перейдите на [официальный сайт Vuforia](https://developer.vuforia.com). \nДля регистрации перейдите на официальный сайт Vuforia и нажмите на кнопку Registerв верхнем правом углу. Вас переместит на страницу регистрации аккаунта.\nЗдесь нужно будет также ввести свой E-mail, Фамилию Имя, пароль, а также указать страну и название учреждения, в котором вы работаете или учитесь. Все данные вводятся на латинице. После введения всех данных отметьте первые две галочки и нажмите на кнопкуCreateAccount',
    'Пример введенных данных ',
    'После этого на указанную вами почту придет письмо от VuforiaDeveloperportal о подтверждении вашего аккаунта. В нем будет указана ссылка, по которой надо перейти для подтверждения аккаунта',
    'Вы подтвердили аккаунт',
    'Теперь вам необходимо войти в него на сайте с помощью ваших данных (E-mailи пароль), по кнопке Log In в верхнем правом углу. После этого нажмите на вкладку Downloads. Далее нажмите на ссылку Add Vuforia to a Unity Project. Начнется скачивание файла Vuforia.unity package.',
    'После того, как загрузка завершится, откроется окно импорта Package (пакетов расширений для Unity). Нажмите кнопку Import ',
    'После завершения всех операций, вы сможете пользоваться объектами VuforiaEngine. Но для их использования потребуется включение настроек в UnityEditor. Для этого откройте UnityEditor, выберите вкладки Edit—Project Settings—Player—XR Settings и поставьте галочку Vuforia Augmented Reality Supported',
    'Далее необходимо получить лицензионный ключ и создать базу изображений для корректной работы Vuforia. Для этого перейдите на [официальный сайт Vuforia](https://developer.vuforia.com) и кликните на вкладку Develop',
    'Для того чтобы получить лицензионный ключ, зайдите в свой созданный аккаунт, и нажмите на кнопку Get Development Key. Дайте название этому ключу ',
    'После этого, данный ключ появится в вашем списке лицензий',
    'Нажмите на созданный ключ. Откроется страница с вашей лицензией. Вы увидите окно с различными символами, кликните на него ',
    'Далее необходимо вернуться обратно в UnityEditor.\nДля начала работы с Vuforia удалите объект Main Camera. Это можно сделать с помощью клавиши Delete или нажав ПКМ и выбрав опцию Delete в контекстном меню',
    'Далее перейдите во вкладку Game Object—Vuforia Engine—AR Camera и выберите эту опцию',
    'При появлении окна нажмите кнопку Import ',
    'Теперь в вашем проекте есть ARCamera, которая является основой работы вашего приложения дополненной реальности. Камера используется непосредственно для отрисовки различных объектов.\nДалее необходимо добавить ключ с сайта Vuforia в приложение. Для этого нажмите на ARCamera, и в окне справа нажмите на Open Vuforia Engine configuration',
    'После этого справа появятся опции камеры, где будет место для добавления ключа с сайта Vuforia, который вы получили ранее. Вставьте ключ с сайта ',
    'Далее необходимо создать базу распознаваемых изображений. Для этого зайдите на [официальный сайт Vuforia](https://developer.vuforia.com). Перейдите во вкладку Develop—Target Manager и нажмите Add Database',
    'В появившемся окне выберите Device и введите имя базы данных. После этого она появится в списке баз данных, нажмите на нее.',
    'Для того, чтобы добавить распознаваемое изображение, нажмите Add Target ',
    'В появившемся окне выберите Single Image, выберите файл на вашем компьютере нужного формата (.jpg или .png), поставьте в поле Width значение 5 и впишите любое имя для изображения ',
    'В дальнейшем, при необходимости, можно также добавлять распознаваемые изображения. После добавления изображений, нажмите Download Database(All) и выберите Unity Editor ',
    'Точно также откройте скачанный файл формата Unity Package и нажмите в появившемся окне Import.\nПерейдите обратно в UnityEditor. Теперь можно начать добавлять распознаваемые объекты в ваш проект. Для этого нажмите правую кнопку мыши на левой панели объектов и выберите Vuforia Engine—Image',
    'После этого добавится изображение, которое будет распознаваться приложением. Для выбора разных распознаваемых изображений необходимо в Image Target Behaviour на вкладке Image Target выбрать другое изображение (если они имеются в базе) ',
    'Чтобы добавить к этому изображению 3D модель, добавьте свой объект в формате .obj в Unity Editor, в нижнюю панель, а потом перенесите данную модель к Image Target как дочерний. В данном случае мы переносим модель призмы из “Методических рекомендаций по использованию ПО Blender”. Для удобства пирамиду собираем из 3 отдельных объектов. В таком случае можно будет отдельно установить разные свойства для сечения и пирамиды. Это необходимо сделать затем, чтобы выставить для них разную прозрачность, с целью наглядного отображения сечения. Этот шаг можно повторять для каждого распознаваемого изображения/объекта.'
],

[
    'Для того чтобы превратить проект из Unity Editor в приложение на Android или IOS нужно совершить «сборку» проекта. Для этого перейдите во вкладку File— Build Settings',
    'В появившемся окне выберите Android/IOS.',
    'Если кнопка Build and Run серая и не нажимается, то сначала нажмите кнопку Switch Platform, а затем кнопку Build ',
    'Далее, выберите место на компьютере где вы хотите сохранить приложение в формате .apk. ',
    'Далее, данный файл в формате .apk переместите на телефон и установите. После установки на телефон и наведения на распознаваемые изображения, вы будете видеть ваши модели. Поздравляем, вы сделали свое приложение с дополненной реальностью!'
],

[
    'Для решения задачи нам понадобится построить вспомогательные точки E, F, G через них проходит сечение, на этом сечении построены отрезки DЕ и FG. Эти два отрезка нужны для расчета площади сечения. Все остальные вспомогательные высоты и отрезки также отчетливо видны на AR-модели. Все это должно помочь визуализировать задачу в 3D пространстве и в результате решить ее.',
    'Рассмотрим все шаги более подробно. В решении задачи мы выделили 5 основных пунктов и наглядно реализовали их в AR-приложении.\n1. Построили изначальную пирамиду ABCDM',
    '2. Отметили точку Е и провели отрезок DE ',
    '3.	Отметили точку P, (пересечение отрезком DE плоскости МАС, также для наглядности провели отрезок МО, где О-центр основания пирамиды. ',
    '4.	Построили отрезок FG параллельный отрезку AC и проходящий через точку P (Точка F принадлежит ребру МА, а G ребру МС)',
    '5.	Получили искомое сечение DGEF и построили его более наглядно, также добавили отрезок DB для наглядности. Далее остается только провести расчеты и получить ответ задачи. Все расчеты и более детальное решение представлено ранее на первом изображении данного блока'
]
)

#endregion

#region blender_text
blender = (
[
    "В рамках учебной программы дисциплины «Индивидуальный проект» школьникам предлагается выполнить проект “оживление учебника” в виде простого AR-приложения для Android-устройства. Именно поэтому в качестве примера мы предлагаем визуализировать фигуру из задачи по стереометрии для ее последующего решения. При пошаговом выполнении всех задач, у вас получится AR-приложение, в котором будет наглядно показана сама фигура и все важные для ее решения точки/линии/высоты. В качестве платформ для разработки были выбраны такие программы, как Blender, Unity 3D и Vuforia."
],

[
    "Blender — профессиональное свободное и открытое программное обеспечение для создания трёхмерной компьютерной графики, включающее в себя средства моделирования, скульптинга, анимации, симуляции, рендеринга, постобработки и монтажа видео со звуком, компоновки с помощью «узлов» (Node Compositing), а также создания 2D-анимаций. В настоящее время пользуется большой популярностью среди бесплатных 3D-редакторов в связи с его быстрым стабильным развитием и технической поддержкой.\nГлавное преимущество ПО Blender состоит в том, что ПО бесплатно, поэтому любой может его скачать и установить для личного пользования."
],

[
    'Для начала работы с Blender требуется установить программу. Перейдите на [официальный сайт](https://www.blender.org/). Нажмите на кнопку DownloadBlender',
    'Выберите вашу операционную систему',
    'Загружаете установочный файл',
    'После скачивания файла откройте его и начните процесс установки. В начале вас встретит приветственное окно, в котором нужно нажать Next',
    'Далее соглашаетесь с лицензионными требованиями, ставите галочку в поле I accept и нажимаете Next ',
    'После снова нажимаете Next',
    'И в следующем окне Install',
    'Подождите пока процесс установки закончится',
    'Нажмите Finish для того чтобы закрыть установщик и перейти к работе с программой'
],

[
    'После запуска программы вас встретит начальное окно, в котором необходимо выбрать в столбце создать файл пункт General и кликнуть на него',
    'После этого откроется среда, в которой и будет происходить работа с моделью. За основу модели автоматически создается куб '
],

[
    'Необходимые базовые принципы работы с Blender:\n1. Для выделения объекта используется левая кнопка мыши\n2. Для рассмотрения объекта с разных сторон необходимо зажать колесико мыши и двигать ей в нужную сторону\n3. Для приближения/отдаления используется колесико мыши.\nВ верхней части программы есть режимы, в которых вы непосредственно и будете работать с моделью. В данной работе вам понадобится всего два из них, а именно Layout и Modeling. В режиме Layout показывается итоговый результат модели, а также в нем вы можете перемещать ее в пространстве. В режиме Modeling вы будете менять размеры и форму модели, а также делить ее на части.'
],

[
    'Фигурой по умолчанию в Blender является куб. Вы можете его как удалить и заменить другой базовой фигурой, так и взять за основу будущей модели.\nВ качестве модели для построения, как мы уже сказали, возьмем фигуру из стереометрической задачи. В ней мы видим пирамиду и построенное сечение, которое и постараемся выделить в дальнейшем в Unity.',
    'В данном примере необходимо будет построить пирамиду, поэтому куб как раз подойдет в качестве основы модели. Для начала перейдите в режим Modeling. Это можно сделать при помощи клавиши TAB или его выборе в контекстном меню. Далее с зажатой клавишей SHIFT выделите четыре верхние вершины куба, кликнув на них ',
    'Далее нажмите сочетание клавиш SHIFT+S, которое откроет меню, где можно различными способами влиять на фигуру. ',
    'После чего выберите Cursor to Selected. Данная функция переместит фокус курсора в центр верхней грани куба.',
    'Далее снова используйте сочетание клавиш SHIFT+S и выберите пункт Selection to Cursor, вследствие чего вершины соединятся в точке, где находился ваш курсор.',
    'В итоге получается пирамида ',
    'В стереометрической задаче, которую мы взяли в качестве примера, на построение нам дана пирамида и сечение. При сохранении файла в программе Blender и последующем открытии его в Unity теряется прозрачность фигуры, которую нам нужно задать, для того чтобы наше сечение было видно под любым углом.\nПоэтому мы разделим нашу пирамиду на 3 части, которыми будут само сечение и части пирамиды, разделенные сечением. В дальнейшем каждой из частей мы зададим прозрачность и свой цвет. Данный процесс будет описан в “Методических рекомендациях по использованию Unity и Vuforia”, а сейчас перейдем к разделению нашей пирамиды на 3 части.\nДля этого перейдите в режим Modeling. В левой части экрана есть различные инструменты для работы с фигурой. Вам необходимо использовать инструмент Нож, который поможет в делении фигуры на части.',
    'Для прямого надреза выберите инструмент нож и кликните на нижнюю вершину пирамиды. После этого нажмите клавишу Z, чтобы перейти в режим, в котором надрез пройдет через всю фигуру. Далее выберите точку на противоположной грани и нажмите правую кнопку мыши ',
    'В итоге получается линия, которая проходит через всю пирамиду – это и будет первый надрез ',
    'Чтобы отсоединить верхнюю часть фигуры, зажмите клавишу Сtrl, выделите верхнюю вершину пирамиды и точки надреза',
    'Далее в верхнем меню выберите Меш — Разделить — Выделение',
    'В итоге получаются две отдельные фигуры ',
    'Далее необходимо переместить верхнюю часть в сторону, чтобы с ней было удобнее работать. Для этого перейдите в режим Layout. В правой части выберите свою фигуру',
    'В левой части программы выберите режим Переместить ',
    'И передвиньте верхнюю часть в сторону ',
    'После того как вы разделили модель на две части, нужно сделать их цельными. Для это перейдите в режим Modeling и выделите 4 точки с зажатой клавишей SHIFT ',
    'Затем в верхнем меню выберите Грань — Заполнить ',
    'Проделайте те же самые шаги для второй модели. В итоге вы получите две цельные фигуры',
    'Вторая фигура',
    'Теперь нужно отрезать от верхней фигуры тонкое сечение, чтобы в дальнейшем в Unity вы могли с ним отдельно работать. Для этого проделайте все то же самое, что и в прошлых пунктах.\nВ конечном итоге должны получиться три фигуры как на образце',
    'После того как вы разделили свою начальную фигуру на три части, сохраните каждый объект отдельно в формате .obj. Чтобы это сделать кликните правой кнопкой мыши по фигуре и нажмите Копировать объекты ',
    'Далее откройте еще одно окно Blender. Удалите начальный объект с помощью клавиши Del и после клика правой кнопкой мыши по экрану, вставьте свою фигуру. Так вам необходимо сделать для всех трех фигур.',
    'После все фигуры необходимо сохранить в формате .obj. Для этого в левом верхнем углу нажмите Файл – Экспортировать – Wavefront(.obj)',
    'У вас откроется окно, в котором нужно выбрать путь файла и нажать кнопку Экспортировать OBJ',
    'В итоге вы получаете три отдельные фигуры: сечение, верхняя часть пирамиды, нижняя часть пирамиды в формате .obj. В дальнейшем мы соединим все 3 части в Unity и зададим им прозрачность и цвет, для того, чтобы получить геометрическую фигуру как в нашей задаче, рассмотренной в качестве примера. Продолжение работы с нашими 3D моделями будет описано в ”Методических рекомендациях по использованию Unity и Vuforia”.'
]
)
#endregion

#endregion


def inline_keyboard_builder_and_image_path(call_data, max):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    next_button = types.InlineKeyboardButton(text="Далее",
                                             callback_data=f"{call_data[0]} {call_data[1]} {call_data[2]} {call_data[3]} {int(call_data[4]) + 1} {max}")
    prv_button = types.InlineKeyboardButton(text="Назад",
                                             callback_data=f"{call_data[0]} {call_data[1]} {call_data[2]} {call_data[3]} {int(call_data[4]) - 1} {max}")
    if int(call_data[4]) != 1:
        keyboard.add(prv_button)
    if int(call_data[4]) != max and int(call_data[4]) != max + 1:
        keyboard.add(next_button)
    return keyboard, f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        call_data = call.data.split(' ')
        max = int(call_data[5])
        if call_data[0] == "rupdImages":
            jpg = ".JPG"
        else:
            jpg = ".jpg"
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{call_data[4]}{jpg}".replace("/block0", "")
        keyboard = inline_keyboard_builder_and_image_path(call_data, max)[0]
        try:
            bot.edit_message_media(message_id=call.message.message_id,
                               chat_id=call.message.chat.id,
                               media=types.InputMedia(type="photo", media=open(image_path, "rb")),
                               reply_markup=keyboard)
            if call_data[0] == 'unityImages':
                bot.edit_message_caption(message_id=call.message.message_id,
                                         chat_id=call.message.chat.id,
                                         caption=unity[int(call_data[1][5]) - 1][int(call_data[4]) - 1],
                                         reply_markup=keyboard)
            if call_data[0] == 'blenderImages':
                bot.edit_message_caption(message_id=call.message.message_id,
                                         chat_id=call.message.chat.id,
                                         caption=blender[int(call_data[1][5]) - 1][int(call_data[4]) - 1],
                                         reply_markup=keyboard)
        except FileNotFoundError:
            return

@bot.message_handler(commands=['start'])
def start_handler(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/menu")
    bot.send_photo(message.from_user.id, caption="Привет! Это бот-помощник по дисциплине Индивидуальный проект. Команда /menu поможет начать\n\nПожалуйста, пользуйтесь меню. Если оно не открылось автоматически, нажмите на кнопку, показанную на картинке.", reply_markup=keyboard, photo=open("startImage.png", "rb"))


@bot.message_handler(commands=['menu'])
def main_menu_handler(message):
    send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
    return bot.register_next_step_handler(send, menu_handler)


def final_menu_block(message, callback_data, current_menu_block_handler):
    call_data = callback_data.split(' ')
    if call_data[0] == "rupdImages":
        jpg = ".JPG"
    else:
        jpg = ".jpg"
    image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}{jpg}".replace(
        "/block0", "")
    keyboard = types.InlineKeyboardMarkup()
    caption = ""
    if int(call_data[4]) <= int(call_data[5]):
        keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
    if call_data[0] == 'unityImages':
        caption = unity[int(call_data[1][5]) - 1][int(call_data[4]) - 2]
    if call_data[0] == 'blenderImages':
        caption = blender[int(call_data[1][5]) - 1][int(call_data[4]) - 2]
    send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard, caption=caption)
    bot.register_next_step_handler(send, current_menu_block_handler)


@bot.message_handler(content_types=['text'])
def menu_handler(message):
    if message.text == 'РУПД':
        send = bot.send_message(message.from_user.id, text=rupd_main_menu_message, reply_markup=rupd_menu_keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == 'Unity':
        send = bot.send_message(message.from_user.id, text=unity_menu_message, reply_markup=unity_menu_keyboard)
        bot.register_next_step_handler(send, unity_menu_handler)
    if message.text == 'Blender':
        send = bot.send_message(message.from_user.id, text=blender_menu_message, reply_markup=blender_menu_keyboard)
        bot.register_next_step_handler(send, blender_menu_handler)
    if message.text == 'Загрузка документов':
        send = bot.send_message(message.from_user.id, text=download_menu_message, reply_markup=download_menu_keyboard)
        bot.register_next_step_handler(send, download_handler)


@bot.message_handler(content_types=['text'])
def download_handler(message):
    if message.text == 'РУПД':
        send = bot.send_document(message.from_user.id, open('RUPD_Individualny_proekt.docx', 'rb'))
        bot.register_next_step_handler(send, download_handler)
    if message.text == 'Unity':
        send = bot.send_document(message.from_user.id, open('Metodicheskie_ukazania_po_Yuniti.docx', 'rb'))
        bot.register_next_step_handler(send, download_handler)
    if message.text == 'Blender':
        send = bot.send_document(message.from_user.id, open('Metodicheskie_rekomendatsii_Blender.docx', 'rb'))
        bot.register_next_step_handler(send, download_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_main_menu_handler(message):
    if message.text == "Пояснительная записка":
        final_menu_block(message, "rupdImages block1 block0 block0 2 5", rupd_main_menu_handler)
    if message.text == "Результаты освоения дисциплины":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_message, reply_markup=rupd_menu_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_handler)
    if message.text == "Содержание учебного предмета":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block3_message, reply_markup=rupd_menu_block3_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_handler)
    if message.text == "Тематическое планирование с указанием количества часов":
        final_menu_block(message, "rupdImages block4 block0 block0 2 2", rupd_main_menu_handler)
    if message.text == "Оценка индивидуального проекта":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message, reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)
    if message.text == "Учебно-методическое обеспечение дисциплины":
        final_menu_block(message, "rupdImages block6 block0 block0 2 1", rupd_main_menu_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)

@bot.message_handler(content_types="text")
def rupd_menu_block2_handler(message):
    if message.text == "Метапредметные результаты":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_block1_message, reply_markup=rupd_menu_block2_block1_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block1_handler)
    if message.text == "Предметные результаты":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_block2_message, reply_markup=rupd_menu_block2_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block2_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_main_menu_message, reply_markup=rupd_menu_keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=["text"])
def rupd_menu_block2_block1_handler(message):
    if message.text == "Регулятивные универсальные учебные действия":
        final_menu_block(message, "rupdImages block2 block1 block1 2 1", rupd_menu_block2_block1_handler)
    if message.text == "Познавательные универсальные учебные действия":
        final_menu_block(message, "rupdImages block2 block1 block2 2 1", rupd_menu_block2_block1_handler)
    if message.text == "Коммуникативные универсальные учебные действия":
        final_menu_block(message, "rupdImages block2 block1 block3 2 1", rupd_menu_block2_block1_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_message, reply_markup=rupd_menu_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=["text"])
def rupd_menu_block2_block2_handler(message):
    if message.text == "Обучаемый получит представление":
        final_menu_block(message, "rupdImages block2 block2 block1 2 1", rupd_menu_block2_block2_handler)
    if message.text == "Обучаемый сможет":
        final_menu_block(message, "rupdImages block2 block2 block2 2 1", rupd_menu_block2_block2_handler)
    if message.text == "Обучаемый научится":
        final_menu_block(message, "rupdImages block2 block2 block3 2 2", rupd_menu_block2_block2_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_message, reply_markup=rupd_menu_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types="text")
def rupd_menu_block3_handler(message):
    if message.text == "Часть 1. Основы проектной деятельности":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block3_block1_message, reply_markup=rupd_menu_block3_block1_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Часть 2. Выполнение обучаемым индивидуального проекта":
        final_menu_block(message, "rupdImages block3 block2 block0 2 3", rupd_menu_block3_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_main_menu_message, reply_markup=rupd_menu_keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block3_block1_handler(message):
    if message.text == "Тема 1. Введение в проектную культуру":
        final_menu_block(message, "rupdImages block3 block1 block1 2 1", rupd_menu_block3_block1_handler)
    if message.text == "Тема 2. Инициализация проекта":
        final_menu_block(message, "rupdImages block3 block1 block2 2 1", rupd_menu_block3_block1_handler)
    if message.text == "Тема 3. Базовое проектирование и исследование":
        final_menu_block(message, "rupdImages block3 block1 block3 2 1", rupd_menu_block3_block1_handler)
    if message.text == "Тема 4. Информационные ресурсы проектной и исследовательской деятельности":
        final_menu_block(message, "rupdImages block3 block1 block4 2 2", rupd_menu_block3_block1_handler)
    if message.text == "Тема 5. Презентация результатов проектной деятельности":
        final_menu_block(message, "rupdImages block3 block1 block5 2 1", rupd_menu_block3_block1_handler)
    if message.text == "Тема 6. Защита результатов проектной и исследовательской деятельности":
        final_menu_block(message, "rupdImages block3 block1 block6 2 1", rupd_menu_block3_block1_handler)
    if message.text == "Тема 7. Коммуникативные навыки":
        final_menu_block(message, "rupdImages block3 block1 block7 2 1", rupd_menu_block3_block1_handler)
    if message.text == "Тема 8. Рефлексия проекта. Индивидуальный прогресс":
        final_menu_block(message, "rupdImages block3 block1 block8 2 1", rupd_menu_block3_block1_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block3_message, reply_markup=rupd_menu_block3_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_handler(message):
    if message.text == "Оценка метапредметных результатов обучения по уровню сформированности Универсальных Учебных Действий (УУД)":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_block1_message, reply_markup=rupd_menu_block5_block1_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Оценка сформированности ключевых компетенций учащихся, которые относятся к общему (метапредметному) содержанию образования":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_block2_message, reply_markup=rupd_menu_block5_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block2_handler)
    if message.text == "Оценка сформированности ключевых компетенций учащихся «4к»":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_block3_message, reply_markup=rupd_menu_block5_block3_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block3_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_main_menu_message, reply_markup=rupd_menu_keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_block1_handler(message):
    if message.text == "Требования, устанавленные ФГОС к результатам образования (ФГОС ООО, п.II.8, ФГОС СОО, п.II.6)":
        final_menu_block(message, "rupdImages block5 block1 block1 2 1", rupd_menu_block5_block1_handler)
    if message.text == "Метапредметные результаты включают освоенные обучающимися":
        final_menu_block(message, "rupdImages block5 block1 block2 2 1", rupd_menu_block5_block1_handler)
    if message.text == "Основные особенности оценки личностных, метапредметных и предметных результатов обучения":
        final_menu_block(message, "rupdImages block5 block1 block3 2 2", rupd_menu_block5_block1_handler)
    if message.text == "Особенности индивидуального проекта":
        final_menu_block(message, "rupdImages block5 block1 block4 2 2", rupd_menu_block5_block1_handler)
    if message.text == "Материалы, которые должны быть представлены к защите итогового проекта":
        final_menu_block(message, "rupdImages block5 block1 block5 2 2", rupd_menu_block5_block1_handler)
    if message.text == "Организация защиты проекта":
        final_menu_block(message, "rupdImages block5 block1 block6 2 3", rupd_menu_block5_block1_handler)
    if message.text == "Процедура оценивания сформированности УУД при защите реализованного проекта":
        final_menu_block(message, "rupdImages block5 block1 block7 2 2", rupd_menu_block5_block1_handler)
    if message.text == "Критерии оценивания итогового проекта":
        final_menu_block(message, "rupdImages block5 block1 block8 2 2", rupd_menu_block5_block1_handler)
    if message.text == "Подходы к оцениванию результатов итогового процесса":
        final_menu_block(message, "rupdImages block5 block1 block9 2 1", rupd_menu_block5_block1_handler)
    if message.text == "Уровни сформированности навыков проектной деятельности (интегральный подход)":
        final_menu_block(message, "rupdImages block5 block1 block10 2 2", rupd_menu_block5_block1_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message, reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_block2_handler(message):
    if message.text == "Компетентность отличается":
        final_menu_block(message, "rupdImages block5 block2 block1 2 2", rupd_menu_block5_block2_handler)
    if message.text == "Три уровня компетенций":
        final_menu_block(message, "rupdImages block5 block2 block2 2 1", rupd_menu_block5_block2_handler)
    if message.text == "Ключевые компетенции":
        final_menu_block(message, "rupdImages block5 block2 block3 2 1", rupd_menu_block5_block2_handler)
    if message.text == "Уровни компетенций и способы деятельности учащихся":
        final_menu_block(message, "rupdImages block5 block2 block4 2 3", rupd_menu_block5_block2_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message,
                                reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_block3_handler(message):
    if message.text == "К 2020 году каждый востребованный сотрудник должен будет уметь":
        final_menu_block(message, "rupdImages block5 block3 block1 2 1", rupd_menu_block5_block3_handler)
    if message.text == "Система “4К”":
        final_menu_block(message, "rupdImages block5 block3 block2 2 1", rupd_menu_block5_block3_handler)
    if message.text == "Подробнее о каждом из четырех «К»":
        final_menu_block(message, "rupdImages block5 block3 block3 2 2", rupd_menu_block5_block3_handler)
    if message.text == "Оценка прогресса в критическом мышлении, креативности, коммуникации и кооперации":
        final_menu_block(message, "rupdImages block5 block3 block4 2 3", rupd_menu_block5_block3_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message,
                                reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)

@bot.message_handler(content_types=['text'])
def unity_menu_handler(message):
    if message.text == "Вспомним предыдущие шаги":
        final_menu_block(message, "unityImages block1 block0 block0 2 1", unity_menu_handler)
    if message.text == "Установка Unity":
        final_menu_block(message, "unityImages block2 block0 block0 2 3", unity_menu_handler)
    if message.text == "Регистрация":
        final_menu_block(message, "unityImages block3 block0 block0 2 5", unity_menu_handler)
    if message.text == "Установка Unity Editor":
        final_menu_block(message, "unityImages block4 block0 block0 2 5", unity_menu_handler)
    if message.text == "Установка Vuforia и добавление в Unity":
        final_menu_block(message, "unityImages block5 block0 block0 2 24", unity_menu_handler)
    if message.text == "Сборка проекта":
        final_menu_block(message, "unityImages block6 block0 block0 2 5", unity_menu_handler)
    if message.text == "Решение задачи":
        final_menu_block(message, "unityImages block7 block0 block0 2 6", unity_menu_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def blender_menu_handler(message):
    if message.text == "Почему":
        final_menu_block(message, "blenderImages block1 block0 block0 2 1", blender_menu_handler)
    if message.text == "Что такое Blender":
        final_menu_block(message, "blenderImages block2 block0 block0 2 1", blender_menu_handler)
    if message.text == "Скачивание и установка Blender":
        final_menu_block(message, "blenderImages block3 block0 block0 2 9", blender_menu_handler)
    if message.text == "Создание файла":
        final_menu_block(message, "blenderImages block4 block0 block0 2 2", blender_menu_handler)
    if message.text == "Основы работы с Blender":
        final_menu_block(message, "blenderImages block5 block0 block0 2 1", blender_menu_handler)
    if message.text == "Создание пирамиды с сечением и подготовка к экспорту в Unity":
        final_menu_block(message, "blenderImages block6 block0 block0 2 25", blender_menu_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


bot.polling(none_stop=True, interval=0)
