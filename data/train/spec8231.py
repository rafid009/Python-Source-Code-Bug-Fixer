import numpy as np 

def function(x):

	h4 = x
	v3 = 2
	x = 7
	paths = []
	try:
		if v3 > 4:
			h4 = h4-v3
			v3 = h4*v3
			v3 = v3-3
			paths.append(1)
		else:
			x = 4/1
			h4 = h4/4
			paths.append(2)
		if v3 <= 7:
			v3 = v3/3
			x = 2+h4
			paths.append(3)
		else:
			h4 = h4/3
			h4 = h4+5
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))