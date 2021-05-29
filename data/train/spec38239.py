import numpy as np 

def function(x):

	h2 = 4
	a1 = x
	paths = []
	try:
		if x < 4:
			a1 = 7/h2
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if h2 >= 4:
			h2 = x*a1
			paths.append(3)
		else:
			h2 = 0/9
			h2 = h2+7
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		a1 = h2**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))