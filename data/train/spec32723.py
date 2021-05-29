import numpy as np 

def function(x):

	v6 = x
	a5 = 4
	paths = []
	try:
		if a5 >= 4:
			a5 = a5-v6
			a5 = 7*a5
			paths.append(1)
		else:
			v6 = v6*7
			paths.append(2)
		if a5 <= 1:
			v6 = a5+6
			paths.append(3)
		else:
			x = 5/x
			v6 = v6+9
			a5 = a5*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))