contacts = {
    'police': 112,
    'emergency':101,
}

while True:
    name = input('🔍Search any contact:')
    if len(name)== 0:
        print("👋 Bye")
    if name in contacts:
            print(f"📞{name}: {contacts[name]}")police
    else:
        print(f "📶 {name}not found")
        ch = input(" Want to add contact? (y/n):")
        if ch== 'y':
            number = input("📞 Enter num")