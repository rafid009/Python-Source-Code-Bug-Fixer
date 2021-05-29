import numpy as np 

def function(x):

	d2 = 7
	i8 = 5
	paths = []
	try:
		if i8 > 1:
			d2 = i8-d2
			d2 = i8+i8
			paths.append(1)
		else:
			d2 = 2-1
			i8 = i8-9
			x = i8+9
			paths.append(2)
		if i8 <= 1:
			i8 = i8/2
			i8 = i8/d2
			i8 = 6-i8
			paths.append(3)
		else:
			d2 = x*4
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))