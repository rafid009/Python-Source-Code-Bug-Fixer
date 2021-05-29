import numpy as np 

def function(x):

	h3 = x
	v2 = x
	paths = []
	try:
		if x < 9:
			x = h3+v2
			paths.append(1)
		else:
			v2 = v2/v2
			x = x*5
			h3 = h3-8
			paths.append(2)
		if v2 <= 2:
			v2 = h3+9
			x = x-x
			h3 = h3-x
			paths.append(3)
		else:
			v2 = v2-v2
			x = h3*x
			h3 = h3*x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))