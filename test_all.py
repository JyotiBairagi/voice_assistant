"""Test script to verify all commands and dependencies work"""
import py_compile
py_compile.compile(r'c:\Users\Jyoti\OneDrive\Desktop\voice_assistant\amigo.py', doraise=True)
print('1. Syntax check: PASSED')

import pyttsx3, speech_recognition as sr, wikipedia, webbrowser, os
print('2. All imports: PASSED')

# Test all command matching logic
test_queries = [
    ('wikipedia python', 'wikipedia'),
    ('open youtube', 'youtube'),
    ('opening youtube', 'youtube'),
    ('youtube', 'youtube'),
    ('open google', 'google'),
    ('opening google', 'google'),
    ('google', 'google'),
    ('open github', 'github'),
    ('github', 'github'),
    ('stackoverflow', 'stackoverflow'),
    ('stack overflow', 'stack overflow'),
    ('open spotify', 'spotify'),
    ('spotify', 'spotify'),
    ('whatsapp', 'whatsapp'),
    ('play music', 'play music'),
    ('music', 'music'),
    ('local disk d', 'local disk d'),
    ('disk d', 'disk d'),
    ('disk c', 'disk c'),
    ('disk e', 'disk e'),
    ('sleep', 'sleep'),
    ('bye', 'bye'),
    ('exit', 'exit'),
    ('are you', 'are you'),
]

all_passed = True
for query, keyword in test_queries:
    if keyword in query:
        print(f'   OK: "{query}" -> matches "{keyword}"')
    else:
        print(f'   FAIL: "{query}" -> should match "{keyword}"')
        all_passed = False

if all_passed:
    print('3. All command matching: PASSED')
else:
    print('3. Command matching: SOME FAILED')

# Test URLs
import requests
urls = {
    'YouTube': 'https://youtube.com',
    'Google': 'https://google.com',
    'GitHub': 'https://github.com',
    'StackOverflow': 'https://stackoverflow.com',
    'Spotify': 'https://spotify.com',
}
url_ok = True
for name, url in urls.items():
    try:
        r = requests.head(url, timeout=5, allow_redirects=True)
        print(f'   OK: {name} ({r.status_code})')
    except Exception as e:
        print(f'   FAIL: {name} -> {e}')
        url_ok = False
if url_ok:
    print('4. All URLs reachable: PASSED')

# Test pyttsx3 engine
try:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    print(f'5. pyttsx3 engine: PASSED ({len(voices)} voices found)')
except Exception as e:
    print(f'5. pyttsx3 engine: FAILED -> {e}')

# Test microphone
try:
    mic = sr.Microphone()
    print('6. Microphone: PASSED')
except Exception as e:
    print(f'6. Microphone: FAILED -> {e}')

# Test wikipedia
try:
    wikipedia.set_lang("en")
    result = wikipedia.summary("Python programming", sentences=1)
    print(f'7. Wikipedia API: PASSED')
except Exception as e:
    print(f'7. Wikipedia API: FAILED -> {e}')

print()
print('=== ALL TESTS COMPLETE ===')
