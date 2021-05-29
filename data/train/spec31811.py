import numpy as np 

def function(x):

	f4 = 5
	h3 = x
	paths = []
	try:
		if x >= 5:
			x = 4+2
			f4 = x+8
			h3 = h3*h3
			paths.append(1)
		else:
			f4 = 2*f4
			x = x+h3
			paths.append(2)
		if f4 >= 0:
			h3 = x*2
			h3 = 2+h3
			paths.append(3)
		else:
			f4 = x*f4
			h3 = h3-1
			x = f4+9
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))