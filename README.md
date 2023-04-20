FeelWeather
=============================

Проект призванный помочь метео зависимым понять от чего именно зависит их самочувствие.
Включает прогноз погоды с цветными алертами и календарь с историей самочувствия для последующего анализа.
Проект существует в видео Django проекта и доступен в сети.

> На данный момент проект доступен по адресу https://feelweather.click


##Мотив
Я давно заметил что часто мое самочувствие зависит от погоды, но заходя на погодные сайты - мне было всегда 
сложно понять, а на какие именно параметры реагирует мое тело ? Какие параметры в норме? А какие сейчас выше
обычного? А есть ли вообще на этих сайтах эти параметры? Также начав изучать тему влияния погоды я начал
понимать что не только параметры земной погоды влияют на самочувствие, есть так называемая космическая 
погода - это активность солнечных бурь, и этот параметр крайне редко встречается на сайтах с погодой.

##Решение
Начав изучать программирование я понял что вместо путешествия по нескольким сайтам с погодной информацией и
попыткой их обьединить в голове, я смогу автоматизировать этот процесс. Сначала я сделал программу в виде 
консольного приложения которую я мог запускать только у себя. После того как я убедился что представление 
данных которое я выбрал удобно (только необходимые параметры и цветовая индикация) и после анализа данных
которые я собирал с своем самочувствии показали определенную корреляцию - я решил сделать общедоступное 
веб-приложение, в котором, я сохраню принцип минималистичности данных с цветовой индикацией параметров 
которые выходят за норму и могут влиять на здоровье. Также я перенес в приложение идею самостоятельного 
анализа данных пользователем, также как и я делал анализ над своими данными.

##Параметры
Далее - нужно было понять, какие именно параметры влияют на самочувствие, а какие не обладают этим свойством
и могут быть отброшены. Еще до создания этого сайта, у меня была экспериментальная версия этого приложения 
для командной строки, в которой я также как и тут, наблюдал параметры погоды и делал записи самочувствия 
с слепками погоды на данный момент. Я проводил наблюдения в течении пяти месяцев. И вот что я выяснил за это время.

###Параметры наиболее сильно влияющие на самочувствие

####Скорость порывов ветра 
- сначала, было не совсем понятно как порывы ветра могут оказывать влияние на самочувствие.
Но на анализе данных было совершенно точно видно корреляцию. Я пришел к выводу, что порывы ветра создают очень 
быструю, в несколько секунд, знакопеременную смену атмосферного давления. Это как если вас мгновенно перемещать
на вершину горы и через секунду возвращать обратно, и так делать продолжительное время. 
Такое воздействие оказывает сильно влияние на людей со слабой сосудистой системой (один из факторов метеозависимости).

###Скорость ветра 
- оказывает влияние по той-же причине, что и порывы, но в меньшей степени. Изменение направление
ветра и его изменчивость также создает относительно быстрые перемены локального давления

###Атмосферное давление
- как мне уже стало понятно, основная причина ухудшения самочувствия и кроется в атмосферном 
давлении, но сам по себе параметр атмосферного давления показывает крайне усредненную по времени картину,
он не покажет моментальное значение давление - усреднение идет с выборкой в районе часа.
Этот параметр имеет значение когда давление находится значительно выше или ниже от нормы в течении долгого времени.

###k - Index 
- это планетарный индекс силы электромагнитного влияния солнца на землю.
По информации статьи https://ehjournal.biomedcentral.com/articles/10.1186/s12940-019-0516-0
геомагнитные возмущения, вызванные солнечной активностью, повышают риск общей смертности и 
смертности от сердечно-сосудистых заболеваний.

###Температура воздуха 
- прямого влияние не имеет, если-б это было так - то мы бы испытывали 
недомогания каждый раз когда выходим из дома зимой.

###Влажность 
- прямой связи на данный момент я не заметил

###Фаза луны 
- прямой связи пока не найдено

##Данные

Итак, я понял круг параметров который необходим для построения приложения для прогноза самочувствия, это:

    -Порывы ветра
    -Скорость ветра
    -атмосферное давление
    -планетарный k-index

Основные параметры текущей погоды и прогноз кроме k-index я взял у
поставщика погодных данных `[weatherapi.com](http://weatherapi.com)` - 
данные берутся по api в формате json. Данные космической погоды берутся на сайте 
Space Weather Prediction Center NOAA [https://www.swpc.noaa.gov/](https://www.swpc.noaa.gov/) 
отдельно в виде прогноза и текущее состояние, так-же в формате json.

##Обработка
Данные со всех трех источников объединяются в один поток данных. Также для удобства добавляем
в данные параметр давления в формате миллиметров ртутного столба.

##Индикаторы
Это одна из важных сторон функционала приложения: Индикаторы позволяют с одного взгляда 
сразу понять выходят ли какие-либо параметры за пределы нормальных или вовсе экстремальные.
Индикаторы позволяют вам не гадать 25 м/с - это много или мало? 750мм/рт.с - Это нормально ли нет ?

###Желтый - параметр повышен.
###Красный - значение уже может оказывать влияние на самочувствие.

Пороговые значения для параметров не фиксированны и я их могу со временем подстраивать.
В перспективе есть идея предоставить каждому пользователю настраивать свои личные пороговые
значения, если есть такая необходимость. Все нужные данные проходят сравнение с моделью 
индикаторов и в общие данные добавляется новый параметр **“alert”** для каждого параметра. 
Таким образом алерты могут быть также доступны по API.

###Сводный индикатор

В процессе работа над общим индикатором прогноза на день - который позволит вообще не
вникать в параметры прогноза - а одной цифрой и цветом показать вероятность ухудшения самочувствия.

###Анализ данных

Анализ данных разделен на два концептуально разных подхода.

###Самостоятельно 
- на сайте в правом верхнем углу есть ссылка на историю вашего самочувствия 
- вы там видите дату, параметры и свое состояние (если вы зарегистрированны и заполняете 
- форму под прогнозом). На основании этих наблюдений вы можете делать самостоятельные 
- выводы о реакции своего организма на погоду. В последствии планируется добавить 
- инструментов анализа в этот раздел

###Глобальный анализ 
- По прошествию года после запуска сайта я планирую собрать все 
накопленные обезличенные данные и подвергнуть их анализу как инструментальному, так и с помощью нейросети. 
Все данные в обезличенном виде будут доступны всем заинтересованным.


  
Код
-----------

Описание Django App:

        /all_requests     - сохраняем в базу все запросы на сайте
        /checklocation    - проверяем наличие города
        /convert_data     - конвертируем bm в мм и добавляем в словарь
        /feel_data        - сохраняем данные о самочувствии в базу
        /get_k_index      - получаем K-index текущий и прогноз. Вставляем в словарь
        /getlocation      - Получаем город запроса
        /getweather       - выводим прогноз на страницу
        /index_view       - выводим главную страницу
        /insert_alerts    - проходимся во всему словарю и вставляем алерты
        /my_feel_history  - выводим историю записей самочувствия
        

Дальше
-----------

 - создание Api сокета для мобильного приложения
 - приведение визуальной части в порядок
 - добавление инструментов анализа в личный кабинет (сортировка, цветовые индикаторы)
 - Добавить выбор города при совпадении названий
 - гео IP
 - форма должна запоминать выбор юзера
 

Виталий (vetrof)

vetrof@gmail.com

https://t.me/vetroffoto

https://twitter.com/vetroff

https://vetrof.com

https://vetrof.ru

