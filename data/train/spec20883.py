import numpy as np 

def function(x):

	v2 = 2
	h4 = x
	x = 9
	paths = []
	try:
		if v2 <= 9:
			x = x/9
			paths.append(1)
		else:
			x = x*5
			h4 = h4/v2
			x = v2/x
			paths.append(2)
		if x < 4:
			h4 = h4*6
			v2 = 0-v2
			paths.append(3)
		else:
			v2 = 6*v2
			h4 = 2*h4
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		v2 = h4**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))