import numpy as np 

def function(x):

	i8 = x
	o5 = x
	paths = []
	try:
		if i8 >= 6:
			o5 = o5-i8
			x = i8*8
			x = x/5
			paths.append(1)
		else:
			o5 = 5-o5
			i8 = i8/2
			paths.append(2)
		if o5 > 3:
			i8 = o5*5
			i8 = 8/i8
			i8 = 0-i8
			paths.append(3)
		else:
			i8 = i8+9
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