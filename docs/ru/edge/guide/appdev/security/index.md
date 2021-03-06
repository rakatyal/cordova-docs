---
license: Licensed to the Apache Software Foundation (ASF) under one
         or more contributor license agreements.  See the NOTICE file
         distributed with this work for additional information
         regarding copyright ownership.  The ASF licenses this file
         to you under the Apache License, Version 2.0 (the
         "License"); you may not use this file except in compliance
         with the License.  You may obtain a copy of the License at

           http://www.apache.org/licenses/LICENSE-2.0

         Unless required by applicable law or agreed to in writing,
         software distributed under the License is distributed on an
         "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
         KIND, either express or implied.  See the License for the
         specific language governing permissions and limitations
         under the License.
---

# Руководство по безопасности

Следующее руководство содержит некоторые рекомендации по безопасности, которые следует учитывать при разработке приложений Cordova. Имейте в виду, что безопасность-это очень сложная тема, и поэтому это руководство не является исчерпывающим. Если вы считаете, что вы можете внести свой вклад в это руководстве, пожалуйста, не стесняйтесь создать запрос в баг трекере Cordova в разделе [«Documentation»][1]. Это руководство предназначено, чтобы быть применимым к любой разработке на Cordova (все платформы), но следует отметить некоторые особенности платформ.

 [1]: https://issues.apache.org/jira/browse/CB/component/12316407

## В данном руководстве рассматриваются следующие темы:

*   Список разрешенных ресурсов
*   IFRAME и механизм идентификатора обратного вызова
*   Закрепление сертификата
*   Самозаверенные сертификаты
*   Шифрованное хранилище
*   Общие советы
*   Рекомендуемые статьи и другие ресурсы

## Список разрешенных ресурсов

*   Прочтите и разберитесь в разделе "Инструкция по доступу к внешним ресурсам"

*   Резрешение определенных доменов не работает на Android API 10 и ниже, и в WP8 для iframe и XMLHttpRequest. Это значит, злоумышленник может загрузить любой домен в iframe и любой сценарий на странице внутри iframe и получить непосредственный доступ к Cordova JavaScript-объектам и соответствующим Java-объектам. Вы должны принять это во внимание при создании приложений для этих платформ. На практике это означает, что вы должны убедится, что вы разрабатываете для Android API версии выше 10, и по возможности не использовать iframe для загрузки внешнего содержимого - используйте плагин inAppBrowser или другие сторонние плагины.

## IFRAME и механизм идентификатора обратного вызова

Если содержимое подается в iframe из whitelisted домена, этот домен будет иметь доступ к родной мост Кордова. Это означает, что если вы белый сторонние рекламные сети и обслуживать эти объявления через iframe, вполне возможно, что вредоносные объявление будет возможность вырваться из iframe и выполнять вредоносные действия. Из-за этого как правило не следует использовать фреймы если вы контролируете сервера, на котором содержание iframe. Также, обратите внимание, что существуют сторонние плагины доступны для поддержки рекламных сетей. Обратите внимание, что это утверждение верно не для iOS, который перехватывает все, включая iframe соединения.

## Закрепление сертификата

Кордова не поддерживает закрепление истинное свидетельство. Главным препятствием для этого является отсутствие родного API в Android для перехвата соединений SSL для выполнения проверки сертификата сервера. (Хотя это возможно для сертификата, закрепление на Android в Java с помощью JSSE, webview на андроид написан на C++, и соединения сервера обрабатываются webview для вас, поэтому невозможно использовать Java и JSSE там.) Поскольку Apache Cordova предназначен предлагать последовательного интерфейсов API на нескольких платформах, не имея возможности в основных платформ ломает эту последовательность.

Есть способы для закрепления сертификат, как проверка, Открытый ключ сервера (отпечатков пальцев) это ожидаемое значение при запуске приложения или другие неоднократно в течение жизни вашего приложения. Сторонние плагины доступны для Кордова, который может сделать это. Однако это не то же самое, как истинный сертификат, закрепления, который автоматически проверяет ожидаемое значение каждого соединения с сервером.

## Самозаверенные сертификаты

Использование самоподписывающихся сертификатов на вашем сервере не рекомендуется. Если вы желаете SSL, то настоятельно рекомендуется что ваш сервер имеет сертификат, который должным образом подписан известным центром сертификации (центр сертификации). Неспособность true сертификат закрепление делает это важно.

Причина заключается, что принимая самозаверяющие сертификаты обходит проверка цепочки сертификатов, которая позволяет любой сертификат сервера, чтобы считаться допустимым в устройство. Это открывает сообщение man-in--middle атак. Она становится очень легко для хакера не только перехватывать и читать весь обмен данными между устройством и сервером, но и изменять сообщения. Устройство никогда не будут знать, что это происходит потому, что он не проверяет, что сертификат сервера подписан доверенным центром сертификации. Устройство имеет никаких доказательств того, что сервер является кто он ожидает. Из-за легкости делает человек в середине нападение принимая самозаверяющие сертификаты лишь незначительно лучше, чем просто выполнение http вместо https на ненадежной сети. Да, трафик будет зашифрован, но он может быть зашифрован с помощью ключа от man-in--middle, поэтому человек в середине может получить доступ все, так что шифрование бесполезно Кроме пассивных наблюдателей. Пользователи доверять SSL для обеспечения безопасности, и это будет намеренно делать это небезопасно, так что использование SSL становится заблуждение. Если это будет использоваться на доверенной сети (то есть, ты полностью внутри контролируемого предприятия), то до сих пор самозаверяющие сертификаты не рекомендуется. Две рекомендации, содержащиеся в доверенной сети, просто использовать http, потому что сама сеть является доверенным, или для получения сертификата, подписанного доверенным центром сертификации (не самоподписанный). Сеть доверенных или нет.

Принципы, описанные здесь, не являются специфическими для Apache Cordova, они применяются для всех связь клиент сервер.

При запуске Кордова на Android, с помощью `android:debuggable="true"` в приложения манифест позволит ошибки SSL, например сертификат цепи ошибок проверки на самозаверяющие сертификаты. Так что вы можете использовать самозаверяющие сертификаты в этой конфигурации, но это не конфигурация, которая должна использоваться, когда ваше приложение находится в производстве. Он предназначен для использования только во время разработки приложения.

## Шифрованное хранилище

(TBD)

## Общие советы

### Не использовать Android Пряник!

*   Установите уровень выше, чем 10 мин цели sdk. API 10 является пряник, и пряник больше не поддерживается Google или устройство производителями и поэтому не рекомендуем команды Кордова. 
*   Пряников было показано, чтобы быть небезопасно и один из самых ориентированных мобильных ОС [http://www.mobilemag.com/2012/11/06/andriod-2-3-gingerbread-security/][2]. 
*   Белый на андроиде не работает с пряников или ниже. Это означает, что злоумышленник может загрузить вредоносный код в iframe, который затем будет иметь доступ ко всем API, Кордова и могли бы использовать этот доступ для кражи личных данных, отправлять SMS-сообщения на платные номера и выполнения других вредоносных действий. 

 [2]: http://bgr.com/2012/11/06/android-security-gingerbread-malware/

### Используйте InAppBrowser для внешних ссылок

*   Использование InAppBrowser при открытии ссылки на любой внешний веб-сайт. Это гораздо безопаснее, чем белый, имя домена и включая содержимое непосредственно в приложении, потому что InAppBrowser будет использовать функции безопасности родной браузер и веб-сайт не даст доступ к среде Кордова. Даже если вы доверяете веб-сайт третьей стороны и включить его непосредственно в приложении, что веб-сайт третьей стороны можно связать с вредоносного веб-содержимого. 

### Проверка всех входных данных пользователя

*   Всегда проверяют все данные, что приложение принимает. Это включает в себя имена пользователей, пароли, даты, загруженных средств массовой информации и т.д. Поскольку злоумышленник может манипулировать HTML и JS активы (либо декомпиляции приложения или с помощью средств отладки как chrome://inspect), эта проверка следует также выполнить на вашем сервере, особенно перед передачей данных в любой серверной службе. 
*   Другие источники, где данные должны быть проверены: документы пользователей, контактов, push-уведомления

### Не кэшируйте конфиденциальные данных

*   Если имена пользователей, пароль, геолокации информацию и другие важные данные находятся в кэше, он мог бы потенциально быть получены позднее неавторизованным пользователем или приложением.

### Не используйте функцию eval(), за исключением случаев если вы знаете, что вы делаете

*   Функция eval() JavaScript имеет долгую историю злоупотребляют. Неправильное использование может открыть код для атак, отладка трудности и медленнее выполнение кода. 

### Не думайте, что ваш исходный код является безопасным

*   Поскольку Cordova-приложение строится на основе HTML и JavaScript, которые упаковываются в контейнере платформы, не следует считать ваш код безопасным. Это позволяет произвести реверс-инжиниринг Cordova-приложения. 

## Рекомендуемые статьи и другие ресурсы

*   [HTML5 безопасности шпаргалку, подробно как для защиты приложения HTML5][3]
*   [PhoneGap и статьи о безопасности устройства, например с помощью зашифрованных данных][4]
*   [Официальный документ о безопасности хорошо известны недостатки в Webview на основе гибридных приложений][5]

 [3]: https://www.owasp.org/index.php/HTML5_Security_Cheat_Sheet
 [4]: https://github.com/phonegap/phonegap/wiki/Platform-Security
 [5]: http://www.cis.syr.edu/~wedu/Research/paper/webview_acsac2011.pdf