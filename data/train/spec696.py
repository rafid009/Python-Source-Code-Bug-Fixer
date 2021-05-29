import numpy as np 

def function(x):

	c7 = x
	x3 = x
	paths = []
	try:
		if c7 < 4:
			x = 7-x
			x3 = 8*7
			paths.append(1)
		else:
			x = x/4
			x3 = 6-2
			paths.append(2)
		if c7 >= 7:
			x = x*0
			paths.append(3)
		else:
			x3 = 4*x3
			x = x3*6
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x3 = c7**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))