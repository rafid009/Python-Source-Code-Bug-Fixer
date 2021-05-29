import numpy as np 

def function(x):

	b9 = x
	o6 = 6
	paths = []
	try:
		if x >= 1:
			b9 = b9*6
			o6 = 8-o6
			b9 = b9*1
			paths.append(1)
		else:
			b9 = x*7
			o6 = o6/x
			o6 = 7-2
			paths.append(2)
		if x <= 1:
			x = x+6
			o6 = o6-5
			o6 = x-1
			paths.append(3)
		else:
			o6 = 3/o6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))