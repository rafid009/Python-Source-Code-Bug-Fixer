import numpy as np 

def function(x):

	f1 = 0
	c9 = x
	paths = []
	try:
		if c9 >= 6:
			c9 = 8-f1
			paths.append(1)
		else:
			f1 = f1-c9
			x = x+2
			paths.append(2)
		if f1 >= 7:
			f1 = f1+4
			x = x+3
			paths.append(3)
		else:
			x = 7+x
			c9 = 7+c9
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		f1 = c9**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))