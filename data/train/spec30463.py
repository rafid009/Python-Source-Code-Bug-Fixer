import numpy as np 

def function(x):

	d5 = 3
	i8 = 0
	paths = []
	try:
		if x <= 2:
			i8 = i8-3
			d5 = 9+d5
			i8 = 7+2
			paths.append(1)
		else:
			d5 = d5*7
			i8 = i8-7
			paths.append(2)
		if i8 <= 7:
			i8 = i8+x
			paths.append(3)
		else:
			i8 = 6/x
			d5 = d5/i8
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))