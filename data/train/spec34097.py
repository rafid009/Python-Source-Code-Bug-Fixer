import numpy as np 

def function(x):

	c5 = 2
	v8 = x
	paths = []
	try:
		if v8 >= 2:
			v8 = v8*0
			x = 8-c5
			v8 = x+v8
			paths.append(1)
		else:
			c5 = 1*5
			paths.append(2)
		if v8 <= 0:
			x = 1/x
			c5 = 2-c5
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))