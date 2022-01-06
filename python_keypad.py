def position(char, keypad_array,width):
    index = keypad_array.index(char)
    i = index//width
    j = index%width
    #print(char,index, i,j)
    return i,j
        
    
def print_path(string,keypad_array,width,height):
    ini_w,ini_h=0,0
    fin_w,fin_h=0,0
    steps=0
    print("\n")
    i=0
    result='Shortest Path ->\n\n'
    while i<len(string):
        fin_w,fin_h = position(string[i],keypad_array,width)
        if i==0:
            result = result +" From   to " +string[i]+"  Path ==> "
        else:    
            result= result+" From "+string[i-1]+" to "+string[i]+"  Path ==> "
        
        if ini_h<fin_h:
            temp=fin_h-ini_h
            if temp<=int(height/2):
                j=0
                while j<temp:
                    result+=("right ")
                    j+=1
                    steps+=1
                    
            else:
                j=height
                while j>temp:
                    result+=("left ")
                    j-=1
                    steps+=1
        elif ini_h>fin_h:
            temp=ini_h-fin_h
            if temp<=int(height/2):
                j=0
                while j<temp:
                    result+=("left ")
                    j+=1
                    steps+=1
                    
            else:
                j=height
                while j>temp:
                    result+=("right ")
                    j-=1
                    steps+=1
                    
        if ini_w<fin_w:
            temp = fin_w-ini_w
            if temp<int(width/2):
                j=0
                while j<temp:
                    result+=("down ")
                    j+=1
                    steps+=1
            else:
                j=width
                while j>temp:
                    result+=("up ")
                    j-=1
                    steps+=1
        elif ini_w>fin_w:
            temp = ini_w-fin_w
            if temp<int(width/2):
                j=0
                while j<temp:
                    result+=("up ")
                    j+=1
                    steps+=1
            else:
                j=width
                while j>temp:
                    result+=("down ")
                    j-=1
                    steps+=1
            
        i+=1    
        ini_w=fin_w
        ini_h=fin_h
        result+=("\n")
    result= result+"\n No:of steps = "+str(steps)
    return result
             
             
             
keypad_array="123+456-789*.0=/"
width, height=4,4
arr = [[0]*width]*height
temp=0;

def print_keyboard(keypad_array,arr,width):
    keyboard='\n'
    #keyboard+=("\nKeypad Layout\n\n")
    i=0
    j=0
    while i<len(keypad_array):
        keyboard+=(keypad_array[i]+'\t')
        arr[j][i%width]=keypad_array[i]
        i+=1
        if i%width==0:
            keyboard+=("\n")
            j+=1
    return keyboard        
            
#print(print_keyboard(keypad_array,arr))       
#print("key-",arr)        
        
#print("Enter the expression : ",end='')
#string=input() 
#print("Expression -",string,"with length",len(string))       
#print(print_path(string,keypad_array,width,height))


        
                    
                
    