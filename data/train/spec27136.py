import numpy as np 

def function(x):

	a2 = 0
	h1 = 8
	paths = []
	try:
		if a2 >= 1:
			h1 = x/h1
			x = 0/4
			paths.append(1)
		else:
			h1 = h1+0
			a2 = 4+a2
			a2 = 2+a2
			paths.append(2)
		if x >= 6:
			a2 = 7-9
			a2 = x*a2
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))