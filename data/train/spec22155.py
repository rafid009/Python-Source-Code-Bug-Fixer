import numpy as np 

def function(x):

	h6 = x
	j0 = x
	paths = []
	try:
		if j0 > 9:
			j0 = 5+j0
			j0 = 8+j0
			x = j0/5
			paths.append(1)
		else:
			j0 = j0+x
			j0 = j0+2
			paths.append(2)
		if x > 6:
			h6 = 4*0
			h6 = h6+h6
			j0 = 9-j0
			paths.append(3)
		else:
			h6 = h6/2
			h6 = 6*x
			x = x*x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		h6 = j0**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))