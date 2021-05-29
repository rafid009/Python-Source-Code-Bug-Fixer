import numpy as np 

def function(x):

	a6 = x
	u9 = 0
	paths = []
	try:
		if u9 > 4:
			x = 5*0
			paths.append(1)
		else:
			x = 4-x
			a6 = 2/a6
			paths.append(2)
		if a6 < 6:
			x = x+x
			paths.append(3)
		else:
			a6 = a6*2
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