import numpy as np 

def function(x):

	v4 = 9
	h4 = 0
	x = x
	paths = []
	try:
		if v4 < 2:
			h4 = h4*2
			v4 = 3+2
			h4 = h4+8
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if h4 > 2:
			v4 = 2+v4
			x = x-8
			paths.append(3)
		else:
			h4 = h4-9
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		v4 = h4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))