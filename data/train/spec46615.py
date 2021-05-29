import numpy as np 

def function(x):

	h1 = 2
	q2 = x
	paths = []
	try:
		if q2 > 5:
			q2 = 0+x
			x = x-x
			paths.append(1)
		else:
			q2 = q2+9
			h1 = h1+h1
			paths.append(2)
		if x >= 0:
			h1 = 4*h1
			h1 = 9-8
			paths.append(3)
		else:
			h1 = h1*h1
			h1 = x*8
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h1 = h1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))