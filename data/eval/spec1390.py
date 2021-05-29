import numpy as np 

def function(x):

	a3 = x
	v3 = x
	paths = []
	try:
		if x >= 5:
			x = a3/x
			x = x+v3
			v3 = v3+3
			paths.append(1)
		else:
			a3 = a3-0
			paths.append(2)
		if v3 >= 6:
			v3 = v3/a3
			x = 5-v3
			x = x-7
			paths.append(3)
		else:
			x = 6*x
			x = x*7
			a3 = 5*6
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))