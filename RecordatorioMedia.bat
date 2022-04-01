@ECHO OFF
"C:\Program Files (x86)\Recordatorio\unins000.exe" /VERYSILENT /SUPPRESSMSGBOXES /ALLUSERS
ECHO ============================
ECHO Desintalado Recordatorio
ECHO ============================

curl -k https://192.168.3.13/userfiles/sebastian/cliente-media.exe?download=1 -o "C:\Users\Public\Downloads\cliente-media.exe"
ECHO ============================
ECHO Descarga deberia de haber terminado
ECHO ============================


"C:\Users\Public\Downloads\cliente-media.exe" /VERYSILENT /SUPPRESSMSGBOXES /ALLUSERS



ECHO ============================
ECHO Instalado Recordatorio
ECHO ============================
Del /f "C:\Users\Public\Downloads\cliente-media.exe" 
ECHO ============================
ECHO Instalador eliminado
ECHO ============================




exit 0