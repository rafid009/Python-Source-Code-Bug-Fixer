import numpy as np 

def function(x):

	a6 = x
	d5 = x
	paths = []
	try:
		if d5 <= 8:
			d5 = 2+d5
			paths.append(1)
		else:
			x = 3+6
			paths.append(2)
		if d5 > 5:
			d5 = x*d5
			x = x+8
			paths.append(3)
		else:
			x = x*6
			a6 = a6-0
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))