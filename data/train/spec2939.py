import numpy as np 

def function(x):

	v2 = x
	o9 = 3
	x = 5
	paths = []
	try:
		if v2 >= 9:
			o9 = o9/8
			o9 = x-o9
			paths.append(1)
		else:
			x = 2+x
			x = 1/x
			o9 = o9*9
			paths.append(2)
		if v2 >= 0:
			x = 2-x
			v2 = x/v2
			x = x*4
			paths.append(3)
		else:
			v2 = x+v2
			v2 = v2-v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))