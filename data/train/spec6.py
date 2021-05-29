import numpy as np 

def function(x):

	e4 = x
	v3 = 9
	paths = []
	try:
		if v3 < 7:
			x = v3*x
			v3 = 1-v3
			paths.append(1)
		else:
			x = x/4
			x = e4-6
			e4 = 8+e4
			paths.append(2)
		if v3 <= 1:
			x = 6-e4
			v3 = v3-5
			paths.append(3)
		else:
			x = 1*x
			v3 = v3*0
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))