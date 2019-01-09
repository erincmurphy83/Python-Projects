from graphics import *

def code(encodeType, message, keyword):
    # Shift position iterates through letters of keyword (shift)

    if 'encode' == encodeType:
        cipher = ""
        s_max = len(keyword)
        s = 0
        for ch in message:        
            char = ord(ch) + ord(keyword[s])
            if char < 0:
                char = 90 - ((abs(char)+65)%26)
            if char < 65:
                char = 90 - ((65 - char)%26)
            if char > 90:
                char = 65 + ((char - 90)%26)
            cipher = cipher + chr(char)
            s = s + 1
            if s == s_max:
                s = 0
        return cipher

    else:
        # Shift position iterates through letters of keyword (shift)
        plain = ""
        s_max = len(keyword)
        s = 0    
        for ch in message:
            char = ord(ch) - ord(keyword[s])
            if char < 0:
                char = 90 - ((abs(char)+65)%26)
            if char < 65:
                char = 90 - ((65 - char)%26)
            if char > 90:
                char = 65 + ((char - 90)%26)
            plain = plain + chr(char)
            s = s + 1
            if s == s_max:
                s = 0
        return plain

def main():
    win = GraphWin("Vigenere", 500, 500)
    win.setCoords(0.0, 5.0, 5.0, 0.0)
    
    # Draw the interface
    Text(Point(1,1), "Message to code:").draw(win)
    Text(Point(1,1.5), "   Enter Keyword:").draw(win)
    inputCode = Entry(Point(2.65,1), 20)
    inputCode.setText("")
    inputCode.draw(win)
    inputKey = Entry(Point(2.2,1.5), 10)
    inputKey.setText("")
    inputKey.draw(win)        

    # Draw Encode/Decode button
    encode = Text(Point(1.5,2.5), "Encode").draw(win)
    decode = Text(Point(3.5,2.5), "Decode").draw(win)
    e_button = Rectangle(Point(1,2), Point(2,3)).draw(win)
    d_button = Rectangle(Point(3,2), Point(4,3)).draw(win)

    # Getting mouse click for encode/decode and waiting for elapsed time
    p1 = win.getMouse()
        
    # Change entered code to useable string
    msg = inputCode.getText().upper().split()
    message = ''.join(msg)
    keyword = inputKey.getText().upper()
   
    while True:
        
        # Determines if click is within encode or decode button
        if ((p1.getX() > 1.0) and (p1.getX() < 2.0)):
            process = 'encode'
            code(process, message, keyword)                    
            break
            
        elif p1.getX() > 3.0 and p1.getX() < 4.0 and p1.getY() > 2.0 and p1.getY() < 3.0:
            process = 'decode'
            code(process, message, keyword)
            break
            
        else:
            Text(Point(2.5, 4.5), "Please click one of the message choices.").draw(win)
            time.sleep(.5)
    
    # display output and change buttons
    e_button.undraw()
    d_button.undraw()
    encode.undraw()
    decode.undraw()

    final_message = code(process, message, keyword)
    outputText1 = Text(Point(2.5,2.5),"Resulting message")
    outputText2 = Text(Point(2.5, 2.75), final_message)
        
    outputText1.draw(win)
    outputText2.draw(win)
    
    # Wait for another click to exit
    
    goodbye = Text(Point(2.5,4.5), "Click anywhere to close the window.").draw(win)
    win.getMouse()
    win.close()
    
main()
