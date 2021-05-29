import numpy as np 

def function(x):

	p9 = x
	h2 = x
	paths = []
	try:
		if p9 <= 6:
			x = x-x
			h2 = 0+h2
			paths.append(1)
		else:
			h2 = 1+h2
			paths.append(2)
		if h2 >= 4:
			x = p9*1
			x = p9-x
			paths.append(3)
		else:
			x = x/7
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