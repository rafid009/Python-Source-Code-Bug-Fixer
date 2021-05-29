import numpy as np 

def function(x):

	a4 = 0
	r4 = x
	paths = []
	try:
		if r4 > 1:
			x = 6+1
			paths.append(1)
		else:
			a4 = a4*4
			a4 = a4*7
			paths.append(2)
		if a4 > 7:
			x = 2-a4
			x = 8+7
			a4 = a4-a4
			paths.append(3)
		else:
			r4 = r4+x
			x = r4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))