import numpy as np 

def function(x):

	a1 = x
	r3 = x
	paths = []
	try:
		if x < 4:
			a1 = a1-7
			a1 = a1-r3
			paths.append(1)
		else:
			a1 = a1+a1
			x = x*5
			a1 = a1-4
			paths.append(2)
		if a1 > 6:
			x = x*7
			paths.append(3)
		else:
			r3 = r3+2
			a1 = 7-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))