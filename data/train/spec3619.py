import numpy as np 

def function(x):

	d2 = 7
	i8 = 6
	paths = []
	try:
		if i8 >= 1:
			d2 = d2*4
			paths.append(1)
		else:
			i8 = x+i8
			paths.append(2)
		if i8 >= 5:
			i8 = i8+3
			x = 0+x
			paths.append(3)
		else:
			x = x+x
			x = 4-7
			d2 = d2+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))