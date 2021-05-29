import numpy as np 

def function(x):

	e3 = 8
	x6 = x
	paths = []
	try:
		if e3 <= 2:
			e3 = x6*0
			paths.append(1)
		else:
			x = 4*x
			x = 2*x6
			x = x/6
			paths.append(2)
		if x > 8:
			e3 = e3-5
			x6 = x6-x6
			e3 = x6+x6
			paths.append(3)
		else:
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))