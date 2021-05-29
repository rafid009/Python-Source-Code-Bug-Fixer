import numpy as np 

def function(x):

	v7 = x
	d2 = x
	x = 2
	paths = []
	try:
		if x <= 8:
			v7 = v7-6
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if v7 >= 1:
			v7 = 1*d2
			d2 = d2+9
			paths.append(3)
		else:
			x = v7-2
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		d2 = v7**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))