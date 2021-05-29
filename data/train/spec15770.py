import numpy as np 

def function(x):

	r7 = 7
	a5 = 4
	paths = []
	try:
		if a5 < 1:
			r7 = 3*6
			r7 = a5+r7
			paths.append(1)
		else:
			a5 = 9-r7
			a5 = r7/x
			paths.append(2)
		if r7 > 6:
			x = x+7
			x = x+x
			a5 = r7*5
			paths.append(3)
		else:
			a5 = x-a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))