import numpy as np 

def function(x):

	f4 = 7
	h6 = 0
	paths = []
	try:
		if h6 <= 7:
			f4 = h6+f4
			f4 = f4*h6
			paths.append(1)
		else:
			h6 = h6/3
			x = x*0
			paths.append(2)
		if h6 <= 1:
			h6 = f4-x
			f4 = f4-2
			paths.append(3)
		else:
			x = x/2
			f4 = x*h6
			x = 8-1
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))