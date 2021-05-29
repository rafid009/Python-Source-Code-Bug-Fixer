import numpy as np 

def function(x):

	o6 = x
	b9 = 6
	paths = []
	try:
		if x < 7:
			x = x*6
			x = x-6
			x = x-x
			paths.append(1)
		else:
			b9 = 7-b9
			paths.append(2)
		if x > 8:
			o6 = 9/3
			b9 = 6-x
			paths.append(3)
		else:
			x = 4+2
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