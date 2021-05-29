import numpy as np 

def function(x):

	h1 = 4
	r5 = 7
	paths = []
	try:
		if r5 >= 8:
			r5 = 4+0
			x = 4-x
			r5 = 6+4
			paths.append(1)
		else:
			h1 = h1-2
			h1 = x*9
			h1 = h1*5
			paths.append(2)
		if x <= 6:
			r5 = 3/9
			paths.append(3)
		else:
			x = 5-x
			h1 = h1-h1
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