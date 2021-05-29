import numpy as np 

def function(x):

	c2 = 5
	i8 = 6
	paths = []
	try:
		if i8 >= 4:
			i8 = 1+4
			i8 = x+2
			c2 = c2-i8
			paths.append(1)
		else:
			c2 = i8+c2
			i8 = 8+1
			c2 = i8+c2
			paths.append(2)
		if x <= 7:
			i8 = 9-c2
			paths.append(3)
		else:
			c2 = c2/2
			c2 = c2+7
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		i8 = c2**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))