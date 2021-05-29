import numpy as np 

def function(x):

	v4 = x
	d6 = x
	paths = []
	try:
		if d6 <= 5:
			v4 = 6*v4
			v4 = 3/v4
			d6 = d6+x
			paths.append(1)
		else:
			v4 = x/v4
			paths.append(2)
		if v4 > 6:
			d6 = d6-d6
			paths.append(3)
		else:
			v4 = v4+d6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))