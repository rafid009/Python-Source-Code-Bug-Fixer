import numpy as np 

def function(x):

	h7 = 4
	x6 = x
	x = 4
	paths = []
	try:
		if h7 <= 4:
			x = x-7
			x6 = 1-0
			x = x/4
			paths.append(1)
		else:
			h7 = x6+x6
			x = 3/x
			x6 = x/x
			paths.append(2)
		if x >= 5:
			x6 = x+x6
			paths.append(3)
		else:
			x6 = x6*2
			x = x/x6
			h7 = h7/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))