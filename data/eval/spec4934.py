import numpy as np 

def function(x):

	r6 = 9
	h4 = x
	paths = []
	try:
		if x < 9:
			r6 = h4+r6
			r6 = 5+x
			paths.append(1)
		else:
			r6 = 2/h4
			paths.append(2)
		if h4 < 0:
			h4 = r6*h4
			paths.append(3)
		else:
			h4 = h4-x
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		h4 = r6**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))