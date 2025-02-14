import sys

def somador_on_off():
    total = 0
    active = True
    number = ''
    
    for line in sys.stdin:
        i = 0
        while i < len(line):
            char = line[i]
            if char.isdigit() and active:
                number += char
            else:
                if number:
                    total += int(number)
                    number = ''
                if char.lower() == 'o':
                    if i + 2 < len(line) and line[i:i+3].lower() == 'off':
                        active = False
                    elif i + 1 < len(line) and line[i:i+2].lower() == 'on':
                        active = True
                elif char == '=':
                    print(line[:i+1], end='')
                    print(f">> {total}")
                    i += 1
                    continue
            i += 1
            
        if '=' not in line:
            print(line, end='')
    
    if number:
        total += int(number)
    
    if total > 0:
        print(f">> {total}")

if __name__ == "__main__":
    somador_on_off()
