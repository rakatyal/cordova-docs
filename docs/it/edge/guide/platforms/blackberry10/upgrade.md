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

# L'aggiornamento di BlackBerry 10

Questa guida Mostra come modificare i progetti di BlackBerry per l'aggiornamento da versioni precedenti di Cordova. La maggior parte di queste istruzioni si applicano ai progetti creati con un vecchio set di strumenti da riga di comando che precedono la `cordova` utilità CLI. L'interfaccia della riga di comando per informazioni, vedere come aggiornare la versione di CLI.

## All'aggiornamento 3.6.0 proietta al 4.0.0

Per i progetti non-CLI, eseguire:

        bin/update percorso/per/progetto
    

Per i progetti CLI:

1.  Aggiornamento del `cordova` versione CLI. Vedere l'interfaccia della riga di comando.

2.  Eseguire `cordova platform update blackberry` nei progetti esistenti.

## L'aggiornamento a 3.2.0 da 3.1.0

Per i progetti che sono stati creati con la CLI, cordova:

1.  Aggiornamento il `cordova` versione CLI. Vedere l'interfaccia della riga di comando.

2.  Eseguire `cordova platform update blackberry`

Per i progetti non creati con la CLI di cordova, eseguire:

        bin/update <project_path>
    

## Aggiornamento a 3.1.0 da 3.0.0

1.  Creare un nuovo progetto di Apache Cordova 3.1.0 utilizzando la CLI, cordova, come descritto in l'interfaccia della riga di comando.

2.  Aggiungere le piattaforme per il progetto di cordova, per esempio:`cordova
platform add blackberry10`.

3.  Copiare il contenuto del progetto originale `www` nella directory del `www` cartella alla radice del progetto cordova appena creato.

4.  Copiare o sovrascrivere qualsiasi attività nativo dal progetto originale ( `Resources` , ecc.)

5.  Copia il `config.xml` del file nella `www` directory e rimuovere eventuali definizioni di plugin. È necessario modificare le impostazioni qui piuttosto che all'interno della directory di piattaforma.

6.  Utilizzare lo strumento CLI di cordova per installare il plug-in che è necessario. Si noti che il CLI gestisce tutti i core API come plugin, così che può essere necessario aggiungere. Solo plugin contrassegnato 3.0.0 e soprattutto sono compatibili con il CLI.

7.  Costruire e testare.

Si prega di notare che il CLI supporta la piattaforma BlackBerry10 esclusivamente. Per PlayBook e BBOS, consultate Cordova versione 2.9.0 e sotto.

## Aggiornamento per il CLI (3.0.0) da 2.9.0

1.  Creare un nuovo progetto di Apache Cordova 3.0.0 utilizzando la CLI, cordova, come descritto in l'interfaccia della riga di comando.

2.  Aggiungi il tua piattaforme il progetto di cordova, ad esempio:`cordova
platform add blackberry10`.

3.  Copiare il contenuto del progetto originale `www` directory il `www` directory alla radice del progetto cordova appena creato.

4.  Copiare o sovrascrivere qualsiasi attività nativo dal progetto originale ( `Resources` , ecc.)

5.  Copia il `config.xml` file nel `www` directory e rimuovere eventuali definizioni di plugin. È necessario modificare le impostazioni qui piuttosto che all'interno della directory di piattaforma.

6.  Utilizzare lo strumento CLI di cordova per installare il plug-in che è necessario. Si noti che il CLI gestisce tutti i core API come plugin, così che può essere necessario aggiungere. Solo 3.0.0 plugin sono compatibili con il CLI.

7.  Compilazione e test.

## 2.8.0 all'aggiornamento di progetti a 2.9.0

Per BlackBerry 10:

1.  Scaricare ed estrarre la sorgente di Cordova 2.9.0 in un percorso di directory permanente sul disco rigido, ad esempio`~/Cordova-2.9.0`.

2.  Chiudere eventuali strumenti SDK in esecuzione: Eclipse, Momentics e simili.

3.  Spostarsi nella directory dove avete messo la fonte scaricata sopra, utilizzando un unix come terminal: Terminal. app, Bash, Cygwin, ecc.

4.  Creare un nuovo progetto, come descritto nella Guida di strumento Shell BlackBerry. Questo diventa la casa del progetto aggiornato.

5.  Copiare la vostra fonte di progetti dal vecchio progetto `/ www` nella directory del progetto nuovo `/ www` directory.

6.  Aggiornare il riferimento allo script di Cordova nella `www/index.html` file (e qualsiasi altro file che contengono il riferimento allo script) per puntare al nuovo `cordova.js` file.

Per BlackBerryOS/Playbook:

1.  Scaricare ed estrarre la sorgente di Cordova 2.9.0 a una posizione permanente directory sul disco rigido, ad esempio`~/Cordova-2.9.0`.

2.  Chiudere eventuali strumenti SDK in esecuzione: Eclipse, Momentics e simili.

3.  Spostarsi nella directory dove avete messo la fonte scaricata sopra, utilizzando un unix come terminal: Terminal. app, Bash, Cygwin, ecc.

4.  Creare un nuovo progetto, come descritto nella Guida di strumento Shell BlackBerry. Avete bisogno di beni da questo nuovo progetto.

5.  Copia il `www/cordova.js` file dal nuovo progetto nella `www` ed eliminare il `www/cordova.js` file.

6.  Aggiornare il riferimento allo script di Cordova nella `www/index.html` file (e qualsiasi altro file che contengono il riferimento allo script) per puntare al nuovo `cordova.js` file.

7.  Copia il `native` directory dal nuovo progetto nel progetto esistente, sovrascrivendo il vecchio `native` directory.

8.  Copia il `lib` directory dal nuovo progetto nel progetto esistente, sovrascrivendo il vecchio `lib` directory.

9.  Copia il `cordova` directory dal nuovo progetto nel progetto esistente, sovrascrivendo il vecchio `cordova` directory.

## All'aggiornamento 2.7.0 progetti per 2.8.0

BlackBerry 10 utilizza i nuovi utensili di CLI e gestisce core API come plugin. Le istruzioni di migrano il proprio progetto per un nuovo progetto, anziché l'aggiornamento di un progetto esistente, a causa della complessità di un vecchio progetto di aggiornamento. Inoltre nota che il cordova js script file è ora chiamato 'js' e non contiene una stringa di versione.

1.  Scaricare ed estrarre la sorgente di Cordova 2.8.0 a una posizione permanente directory sul disco rigido, ad esempio`~/Cordova-2.8.0`.

2.  Chiudere eventuali strumenti SDK in esecuzione: Eclipse, Momentics e simili.

3.  Spostarsi nella directory dove avete messo la fonte scaricata sopra, utilizzando un unix come terminal: Terminal. app, Bash, Cygwin, ecc.

4.  Creare un nuovo progetto, come descritto nella Guida di strumento Shell BlackBerry. Questo diventa la casa del progetto aggiornato.

5.  Copiare la vostra fonte di progetti dal vecchio progetto `/ www` nella directory del progetto nuovo `/ www` directory.

6.  Aggiornare il riferimento allo script di Cordova nella `www/index.html` file (e qualsiasi altro file che contengono il riferimento allo script) per puntare al nuovo `cordova.js` file.

Per BlackBerryOS/Playbook:

1.  Scaricare ed estrarre la sorgente di Cordova 2.8.0 a una posizione permanente directory sul disco rigido, ad esempio`~/Cordova-2.8.0`.

2.  Chiudere eventuali strumenti SDK in esecuzione: Eclipse, Momentics e simili.

3.  Spostarsi nella directory dove avete messo la fonte scaricata sopra, utilizzando un unix come terminal: Terminal. app, Bash, Cygwin, ecc.

4.  Creare un nuovo progetto, come descritto nella Guida di strumento Shell BlackBerry. Avete bisogno di beni da questo nuovo progetto.

5.  Copia il `www/cordova.js` file dal nuovo progetto nella `www` ed eliminare il `www/cordova.js` file.

6.  Aggiornare il riferimento allo script di Cordova nel `www/index.html` file (e qualsiasi altro file che contengono il riferimento allo script) per puntare al nuovo `cordova.js` file.

7.  Copia il `native` directory dal nuovo progetto nel progetto esistente, sovrascrivendo il vecchio `native` directory.

8.  Copia il `lib` directory dal nuovo progetto nel progetto esistente, sovrascrivendo il vecchio `lib` directory.

9.  Copia il `cordova` directory dal nuovo progetto nel progetto esistente, sovrascrivendo il vecchio `cordova` directory.

## 2.6.0 all'aggiornamento di progetti a 2.7.0

1.  Scaricare ed estrarre la sorgente di Cordova 2.7.0 in un percorso di directory permanente sul disco rigido, per esempio a `~/Cordova-2.7.0`.

2.  Chiudere eventuali strumenti SDK in esecuzione: Eclipse, Momentics e simili.

3.  Spostarsi nella directory dove messo il sorgente scaricato sopra, utilizzando un unix come terminal: Terminal. app, Bash, Cygwin, ecc.

4.  Creare un nuovo progetto, come descritto nella Guida di strumento Shell BlackBerry. Avete bisogno di beni da questo nuovo progetto.

5.  Copia il `www/cordova-2.7.0.js` file dal nuovo progetto nella `www` ed eliminare il `www/cordova-2.6.0.js` file.

6.  Aggiornare il riferimento allo script di Cordova nel `www/index.html` file (e qualsiasi altro file che contengono il riferimento allo script) per puntare al nuovo `cordova-2.7.0.js` file.

7.  Copia il `native` directory dal nuovo progetto nel progetto esistente, sovrascrivendo il vecchio `native` directory.

8.  Copia il `lib` directory dal nuovo progetto nel progetto esistente, sovrascrivendo il vecchio `lib` directory.

9.  Copia il `cordova` directory dal nuovo progetto nel progetto esistente, sovrascrivendo il vecchio `cordova` directory.

## L'aggiornamento a 2.6.0 da 2.5.0

Aggiornare la directory di download di PhoneGap:

Si consiglia di scaricare una nuova copia di tutta la directory.

Tuttavia, qui ci sono le nuove parti necessarie per l'aggiornamento a fasi:

1.  Aggiornare il file cordova.blackberry.js nel `Phonegap-2.6.0/lib/blackberry/javascript` directory.

2.  Aggiornamento del `ext` , `ext-air` , e `ext-qnx` nel `Phonegap-2.6.0/lib/blackberry/framework` directory.

3.  Aggiornamento il `build.xml` file nel `Phonegap-2.6.0/lib/blackberry` directory.

4.  Aggiornamento il `Phonegap-2.6.0/lib/blackberry/bin` directory.

5.  Aggiornamento il `VERSION` file nel `Phonegap-2.6.0/lib/blackberry` directory.

Nell'esempio di aggiornamento / directory o la migrazione di un esistente progetto:

1.  Apri il `www` directory che contiene l'app.

2.  Rimuovere e aggiornare il file. jar nel `ext/` directory.

3.  Aggiornare il contenuto del `ext-air/` directory.

4.  Aggiornare il contenuto del `ext-qnx/` directory.

5.  Copiare il nuovo `cordova-2.6.0.js` nel vostro progetto.

6.  Aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.6.0.js` file.

## L'aggiornamento a 2.5.0 da 2.4.0

Aggiornare la directory di download di PhoneGap:

Si consiglia di scaricare una nuova copia di tutta la directory.

Tuttavia, qui ci sono le nuove parti necessarie per l'aggiornamento a fasi:

1.  Aggiornare il file cordova.blackberry.js nel `Phonegap-2.5.0/lib/blackberry/javascript` directory.

2.  Aggiornamento del `ext` , `ext-air` , e `ext-qnx` nel `Phonegap-2.5.0/lib/blackberry/framework` directory.

3.  Aggiornamento il `build.xml` file nel `Phonegap-2.5.0/lib/blackberry` directory.

4.  Aggiornamento il `Phonegap-2.5.0/lib/blackberry/bin` directory.

5.  Aggiornamento il `VERSION` file nel `Phonegap-2.5.0/lib/blackberry` directory.

Nell'esempio di aggiornamento / directory o la migrazione di un esistente progetto:

1.  Aperto il `www` directory che contiene l'app.

2.  Rimuovere e aggiornare il file. jar nella `ext/` directory.

3.  Aggiornare il contenuto del `ext-air/` directory.

4.  Aggiornare il contenuto del `ext-qnx/` directory.

5.  Copiare il nuovo `cordova-2.5.0.js` nel vostro progetto.

6.  Aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.5.0.js` file.

## L'aggiornamento a 2.4.0 da 2.3.0

Aggiornamento appena il `www` directory:

1.  Apri il `www` directory che contiene l'app.

2.  Rimuovere e aggiornare il file. jar nel `ext/` directory.

3.  Aggiornare il contenuto del `ext-air/` directory.

4.  Copiare il nuovo `cordova-2.4.0.js` nel vostro progetto.
    
    *   Se playbook, quindi aggiornamento il js file nel `playbook/` directory.
    *   Se BlackBerry 10, quindi aggiornare il file il `qnx/` directory.

5.  Aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.4.0.js` file.

Aggiornando la directory di esempio (cioè, aggiornamento usando gli strumenti della formica):

1.  Apri il `sample/lib/` directory.

2.  Aggiornare il file. jar nel `cordova.2.3.0/ext/` directory.

3.  Aggiornare il contenuto del `cordova.2.3.0/ext-air/` directory.

4.  Aggiornare il contenuto del `cordova.2.3.0/ext-qnx/` directory.

5.  Aggiornare il file il `cordova.2.3.0/javascript/` directory.

6.  Apri il `sample/lib/` directory e Rinomina la `cordova.2.3.0/` directory`cordova.2.4.0/`.

7.  Tipo `ant blackberry build` o `ant playbook build` per aggiornare il `www` directory con Cordova aggiornato.

8.  Apri il `www` directory e aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.4.0.js` file.

## L'aggiornamento a 2.3.0 da 2.2.0

Aggiornando solo il `www` directory:

1.  Apri il `www` directory che contiene l'app.

2.  Rimuovere e aggiornare il file. jar nel `ext/` directory.

3.  Aggiornare il contenuto del `ext-air/` directory.

4.  Copiare il nuovo `cordova-2.3.0.js` nel vostro progetto.
    
    *   Se playbook, quindi aggiornamento il js file nel `playbook/` directory.
    *   Se BlackBerry 10, quindi aggiornare il file il `qnx/` directory.

5.  Aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.3.0.js` file.

Aggiornando la directory di esempio (cioè, aggiornamento usando gli strumenti della formica):

1.  Apri il `sample/lib/` directory.

2.  Aggiornare il file. jar nella `cordova.2.2.0/ext/` directory.

3.  Aggiornare il contenuto del `cordova.2.2.0/ext-air/` directory.

4.  Aggiornare il contenuto del `cordova.2.2.0/ext-qnx/` directory.

5.  Aggiornare il file. js nella `cordova.2.2.0/javascript/` directory.

6.  Aperto il `sample/lib/` directory e rinomina la `cordova.2.2.0/` nella directory`cordova.2.3.0/`.

7.  Tipo `ant blackberry build` o `ant playbook build` per aggiornare il `www` directory con Cordova aggiornato.

8.  Aperto il `www` directory e aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.3.0.js` file.

## Aggiornamento a 2.2.0 da 2.1.0

Aggiornamento solo la directory www:

1.  Aperto il `www` directory che contiene l'app.

2.  Rimuovere e aggiornare il file. jar nella `ext/` directory.

3.  Aggiornare il contenuto del `ext-air/` directory.

4.  Copiare il nuovo `cordova-2.2.0.js` nel vostro progetto.
    
    *   Se playbook, quindi aggiornamento il js file nella `playbook/` directory.
    *   Se BlackBerry 10, quindi aggiornare il file. js nella `qnx/` directory.

5.  Aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.2.0.js` file.

Aggiornando la directory di esempio (cioè, aggiornamento usando gli strumenti della formica):

1.  Aperto il `sample/lib/` directory.

2.  Aggiornare il file. jar nella `cordova.2.1.0/ext/` directory.

3.  Aggiornare il contenuto del `cordova.2.1.0/ext-air/` directory.

4.  Aggiornare il contenuto del `cordova.2.1.0/ext-qnx/` directory.

5.  Aggiornare il file il `cordova.2.1.0/javascript/` directory.

6.  Apri il `sample/lib/` directory e Rinomina la `cordova.2.1.0/` directory`cordova.2.2.0/`.

7.  Tipo `ant blackberry build` o `ant playbook build` per aggiornare il `www` directory con Cordova aggiornato.

8.  Apri il `www` directory e aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.2.0.js` file.

## L'aggiornamento a 2.1.0 da 2.0.0

Aggiornamento appena il `www` directory:

1.  Apri il `www` directory che contiene l'app.

2.  Rimuovere e aggiornare il file. jar nel `ext/` directory.

3.  Aggiornare il contenuto del `ext-air/` directory.

4.  Copiare il nuovo `cordova-2.1.0.js` nel vostro progetto.
    
    *   Se playbook, quindi aggiornamento il js file nel `playbook/` directory.

5.  Aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.1.0.js` file.

Aggiornando la directory di esempio (cioè, aggiornamento usando gli strumenti della formica):

1.  Apri il `sample/lib/` directory.

2.  Aggiornare il file. jar nel `cordova.2.0.0/ext/` directory.

3.  Aggiornare il contenuto del `cordova.2.0.0/ext-air/` directory.

4.  Aggiornare il file il `cordova.2.0.0/javascript/` directory.

5.  Apri il `sample/lib/` directory e Rinomina la `cordova.2.0.0/` directory`cordova.2.1.0/`.

6.  Tipo `ant blackberry build` o `ant playbook build` per aggiornare il `www` directory con Cordova aggiornato.

7.  Apri il `www` directory e aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.1.0.js` file.

## L'aggiornamento a 2.0.0 da 1.9.0

Aggiornamento appena il `www` directory:

1.  Apri il `www` directory che contiene l'app.

2.  Rimuovere e aggiornare il file. jar nel `ext/` directory.

3.  Aggiornare il contenuto del `ext-air/` directory.

4.  Copiare il nuovo `cordova-2.0.0.js` nel vostro progetto.
    
    *   Se playbook, quindi aggiornamento il js file nel `playbook/` directory.

5.  Aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.0.0.js` file.

6.  Aggiornamento il `www/plugins.xml` file. Due plugin cambiato la loro etichetta di servizio/spazio dei nomi. Cambiare le vecchie voci per i plugin di cattura e contatto da:
    
        <plugin name="Capture" value="org.apache.cordova.media.MediaCapture"/>
        <plugin name="Contact" value="org.apache.cordova.pim.Contact"/>
        
    
    VOX
    
        <plugin name="Capture" value="org.apache.cordova.capture.MediaCapture"/>
        <plugin name="Contacts" value="org.apache.cordova.pim.Contact"/>
        

Aggiornando la directory di esempio (cioè, aggiornamento usando gli strumenti della formica):

1.  Apri il `sample/lib/` directory.

2.  Aggiornare il file. jar nel `cordova.1.9.0/ext/` directory.

3.  Aggiornare il contenuto del `cordova.1.9.0/ext-air/` directory.

4.  Aggiornare il file il `cordova.1.9.0/javascript/` directory.

5.  Apri il `sample/lib/` directory e Rinomina la `cordova.1.9.0/` directory`cordova.2.0.0/`.

6.  Tipo `ant blackberry build` o `ant playbook build` per aggiornare il `www` directory con Cordova aggiornato.

7.  Apri il `www` directory e aggiorna il tuo HTML per utilizzare il nuovo `cordova-2.0.0.js` file.

8.  Apri il `www` directory e aggiornamento il `plugins.xml` file. Due plugin cambiato la loro etichetta di servizio/spazio dei nomi. Cambiare le vecchie voci per i plugin di cattura e contatto da:
    
         <plugin name="Capture" value="org.apache.cordova.media.MediaCapture"/>
         <plugin name="Contact" value="org.apache.cordova.pim.Contact"/>
        
    
    VOX
    
         <plugin name="Capture" value="org.apache.cordova.capture.MediaCapture"/>
         <plugin name="Contacts" value="org.apache.cordova.pim.Contact"/>
        

*   Per aggiornare a 1.8.0, si prega di andare da 1.7.0

## Aggiornamento a 1.8.0 da 1.7.0

Aggiornando solo il `www` directory:

1.  Apri il `www` directory che contiene l'app.

2.  Rimuovere e aggiornare il file. jar nel `ext/` directory.

3.  Aggiornare il contenuto del `ext-air/` directory.

4.  Copiare il nuovo `cordova-1.8.0.js` nel vostro progetto.
    
    *   Se playbook, quindi aggiornamento il js file nel `playbook/` directory.

5.  Aggiorna il tuo HTML per utilizzare il nuovo `cordova-1.8.0.js` file.

6.  Aggiornamento il `www/plugins.xml` file. Due plugin cambiato la loro etichetta di servizio/spazio dei nomi. Cambiare le vecchie voci per i plugin di cattura e contatto da:
    
        <plugin name="Capture" value="org.apache.cordova.media.MediaCapture"/>
        <plugin name="Contact" value="org.apache.cordova.pim.Contact"/>
        
    
    VOX
    
        <plugin name="Capture" value="org.apache.cordova.capture.MediaCapture"/>
        <plugin name="Contacts" value="org.apache.cordova.pim.Contact"/>
        

Aggiornare la directory di esempio (vale a dire l'aggiornamento utilizzando gli strumenti di formica):

1.  Apri il `sample/lib/` directory.

2.  Aggiornare il file. jar nel `cordova.1.7.0/ext/` directory.

3.  Aggiornare il contenuto del `cordova.1.7.0/ext-air/` directory.

4.  Aggiornare il file il `cordova.1.7.0/javascript/` directory.

5.  Apri il `sample/lib/` directory e Rinomina la `cordova.1.7.0/` directory`cordova.1.8.0/`.

6.  Tipo `ant blackberry build` o `ant playbook build` per aggiornare il `www` directory con Cordova aggiornato.

7.  Apri il `www` directory e aggiorna il tuo HTML per utilizzare il nuovo `cordova-1.8.0.js` file.

8.  Apri il `www` directory e aggiornamento il `plugins.xml` file. Due plugin cambiato la loro etichetta di servizio/spazio dei nomi. Cambiare le vecchie voci per i plugin di cattura e contatto da:
    
         <plugin name="Capture" value="org.apache.cordova.media.MediaCapture"/>
         <plugin name="Contact" value="org.apache.cordova.pim.Contact"/>
        
    
    VOX
    
         <plugin name="Capture" value="org.apache.cordova.capture.MediaCapture"/>
         <plugin name="Contacts" value="org.apache.cordova.pim.Contact"/>