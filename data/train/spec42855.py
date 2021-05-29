import numpy as np 

def function(x):

	d6 = x
	v3 = x
	x = x
	paths = []
	try:
		if x > 3:
			v3 = 8/v3
			paths.append(1)
		else:
			x = d6*6
			d6 = 7*d6
			paths.append(2)
		if v3 <= 7:
			d6 = d6-0
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))