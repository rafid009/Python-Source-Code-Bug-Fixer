import numpy as np 

def function(x):

	i8 = x
	o4 = 5
	paths = []
	try:
		if o4 <= 4:
			o4 = o4+4
			x = x/6
			paths.append(1)
		else:
			x = x-o4
			i8 = x+i8
			paths.append(2)
		if o4 <= 7:
			i8 = i8+x
			paths.append(3)
		else:
			x = 3-0
			i8 = i8/4
			o4 = i8-o4
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