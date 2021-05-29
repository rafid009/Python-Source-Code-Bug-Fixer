import numpy as np 

def function(x):

	p7 = x
	h5 = 9
	paths = []
	try:
		if p7 > 8:
			x = x*7
			x = 7*p7
			paths.append(1)
		else:
			h5 = 7-h5
			x = x*0
			paths.append(2)
		if p7 < 2:
			x = p7*0
			paths.append(3)
		else:
			x = 4*0
			x = 8-3
			x = 3-1
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))