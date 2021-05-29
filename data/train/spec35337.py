import numpy as np 

def function(x):

	i8 = x
	r9 = 5
	paths = []
	try:
		if i8 >= 7:
			i8 = i8*7
			x = 3/9
			paths.append(1)
		else:
			x = x*8
			i8 = 5/i8
			i8 = 3-8
			paths.append(2)
		if i8 > 1:
			x = i8*x
			i8 = r9-6
			paths.append(3)
		else:
			r9 = x-6
			i8 = i8+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))