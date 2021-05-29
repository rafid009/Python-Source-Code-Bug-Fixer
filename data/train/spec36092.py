import numpy as np 

def function(x):

	c6 = 5
	f4 = 7
	paths = []
	try:
		if f4 <= 4:
			c6 = 0/f4
			paths.append(1)
		else:
			x = f4/x
			paths.append(2)
		if f4 >= 3:
			x = x+c6
			paths.append(3)
		else:
			c6 = c6-2
			f4 = c6+f4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))