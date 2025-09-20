def main():
    # هنا ضع كودك الرئيسي
    # هذا مثال باستخدام Kivy للواجهة
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.boxlayout import BoxLayout
    
    class MyApp(App):
        def build(self):
            layout = BoxLayout(orientation='vertical')
            label = Label(text='مرحبًا! تم بناء هذا التطبيق باستخدام GitHub Actions')
            button = Button(text='اضغط هنا')
            layout.add_widget(label)
            layout.add_widget(button)
            return layout

    # تشغيل التطبيق
    MyApp().run()

# إذا كنت تريد تشغيل الكود مباشرة عند استيراده
if __name__ == "__main__":
    main()
