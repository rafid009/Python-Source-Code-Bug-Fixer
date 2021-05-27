import numpy as np 

def function(x):

	e4 = 5
	u7 = 9
	paths = []
	try:
		if x > 7:
			x = x*x
			x = 3-2
			x = x/x
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if u7 <= 8:
			e4 = e4/u7
			paths.append(3)
		else:
			e4 = 2+u7
			u7 = 3*8
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