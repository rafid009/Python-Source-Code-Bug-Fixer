import numpy as np 

def function(x):

	r3 = x
	h3 = 9
	paths = []
	try:
		if r3 < 8:
			x = x*h3
			h3 = h3*r3
			x = 4+x
			paths.append(1)
		else:
			x = h3+x
			r3 = 2/4
			h3 = h3/7
			paths.append(2)
		if r3 >= 5:
			h3 = 3+h3
			paths.append(3)
		else:
			h3 = h3+7
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		r3 = h3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))