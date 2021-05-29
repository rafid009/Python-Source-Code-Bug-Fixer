import numpy as np 

def function(x):

	d7 = x
	x6 = 9
	paths = []
	try:
		if x > 3:
			d7 = d7*1
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if x < 2:
			x6 = x6*3
			x6 = 9-x6
			x = x+0
			paths.append(3)
		else:
			x6 = x6+9
			x6 = 9/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))