import numpy as np 

def function(x):

	d2 = x
	i8 = 1
	paths = []
	try:
		if i8 >= 2:
			d2 = d2/9
			paths.append(1)
		else:
			x = x+9
			x = 2/x
			x = 6-x
			paths.append(2)
		if i8 <= 5:
			x = x/3
			x = 6*x
			paths.append(3)
		else:
			d2 = d2-7
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		i8 = d2**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))