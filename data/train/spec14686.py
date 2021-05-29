import numpy as np 

def function(x):

	h7 = 8
	r6 = 1
	paths = []
	try:
		if x < 4:
			x = r6*x
			r6 = 3+5
			paths.append(1)
		else:
			h7 = h7-r6
			h7 = 9*x
			paths.append(2)
		if x <= 4:
			x = 4*x
			paths.append(3)
		else:
			r6 = r6-5
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))