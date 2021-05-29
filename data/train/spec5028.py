import numpy as np 

def function(x):

	e6 = 1
	h2 = x
	paths = []
	try:
		if h2 >= 4:
			h2 = h2/1
			e6 = x+1
			paths.append(1)
		else:
			x = h2+3
			e6 = 1*e6
			x = x-7
			paths.append(2)
		if x > 7:
			h2 = e6*e6
			h2 = e6/e6
			paths.append(3)
		else:
			e6 = 0+7
			h2 = h2*9
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))