import numpy as np 

def function(x):

	h3 = 9
	a1 = 6
	paths = []
	try:
		if a1 > 4:
			x = x*x
			x = x/h3
			x = x-2
			paths.append(1)
		else:
			a1 = x*x
			x = x/h3
			paths.append(2)
		if h3 > 9:
			x = x/8
			x = 3+1
			a1 = a1/h3
			paths.append(3)
		else:
			a1 = 9/x
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		h3 = a1**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))