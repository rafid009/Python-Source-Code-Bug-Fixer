import numpy as np 

def function(x):

	a7 = x
	k7 = 8
	paths = []
	try:
		if k7 >= 0:
			x = x*6
			k7 = 9/k7
			a7 = a7/1
			paths.append(1)
		else:
			k7 = k7*1
			k7 = 9-5
			paths.append(2)
		if x <= 1:
			k7 = k7*k7
			x = k7/a7
			a7 = 9-a7
			paths.append(3)
		else:
			a7 = x+x
			k7 = k7+6
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))