# test_import.py
try:
    import botasaurus
    print(f"✅ Botasaurus успешно импортирован! (версия недоступна)")
    
    # Проверим основные компоненты
    from botasaurus import bt
    print("✅ bt успешно импортирован")
    
    # Проверим декораторы
    from botasaurus.browser import browser, Driver
    print("✅ browser и Driver успешно импортированы")
    
    print("🎉 Все импорты работают корректно!")
    print(f"   - Botasaurus установлен: True")
    print(f"   - Декоратор bt доступен: True")
    print(f"   - Классы browser/Driver доступны: True")
    
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")