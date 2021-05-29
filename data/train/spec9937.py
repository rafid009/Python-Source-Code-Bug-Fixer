import numpy as np 

def function(x):

	e5 = x
	k7 = x
	paths = []
	try:
		if e5 > 2:
			x = 5/2
			x = x*e5
			paths.append(1)
		else:
			k7 = k7*x
			k7 = 3*5
			k7 = e5*k7
			paths.append(2)
		if e5 >= 3:
			x = x+e5
			x = 6-x
			k7 = k7*4
			paths.append(3)
		else:
			e5 = x/e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))