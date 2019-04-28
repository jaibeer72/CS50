def square(x): 
    return x*x

def main():
    for i in range(10): 
        print("{} squared is {}".format(i,square(i)))

if __name__ == "__main__": #this basically says only run this main when you are running this file
    main()                  #and not when it is importing some function to some other files 


class Point: 
    def __init__(self,x,y):
        self.x= x
        self.y= y

point=Point(3,5)
print(point.x)

