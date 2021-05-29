import numpy as np 

def function(x):

	h4 = 5
	m2 = 6
	paths = []
	try:
		if h4 > 6:
			h4 = 9*0
			paths.append(1)
		else:
			h4 = h4/8
			paths.append(2)
		if h4 <= 2:
			h4 = x+1
			paths.append(3)
		else:
			h4 = m2+m2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))