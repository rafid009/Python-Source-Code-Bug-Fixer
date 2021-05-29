import numpy as np 

def function(x):

	a1 = x
	a5 = x
	paths = []
	try:
		if x >= 7:
			a5 = a5*8
			paths.append(1)
		else:
			a1 = a1*x
			paths.append(2)
		if a1 > 7:
			x = a1+x
			paths.append(3)
		else:
			a5 = 0*x
			x = a5+x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))