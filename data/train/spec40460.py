import numpy as np 

def function(x):

	v6 = 8
	e3 = x
	paths = []
	try:
		if v6 <= 6:
			v6 = v6-e3
			x = x+x
			v6 = 9*2
			paths.append(1)
		else:
			e3 = x-x
			paths.append(2)
		if v6 > 8:
			v6 = 9/7
			paths.append(3)
		else:
			v6 = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))