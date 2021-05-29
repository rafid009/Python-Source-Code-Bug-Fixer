import numpy as np 

def function(x):

	x9 = x
	d8 = 8
	x = x
	paths = []
	try:
		if d8 < 8:
			d8 = d8/3
			x9 = x9+3
			paths.append(1)
		else:
			x = x*9
			x = 8-x
			x9 = x9+0
			paths.append(2)
		if x9 <= 5:
			x9 = x9+d8
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))