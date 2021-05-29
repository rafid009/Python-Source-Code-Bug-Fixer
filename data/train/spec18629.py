import numpy as np 

def function(x):

	h1 = x
	k5 = x
	paths = []
	try:
		if h1 >= 4:
			k5 = k5*4
			paths.append(1)
		else:
			h1 = k5*h1
			x = 6-9
			paths.append(2)
		if h1 > 6:
			h1 = 4-5
			h1 = k5*0
			h1 = 4*x
			paths.append(3)
		else:
			x = x-k5
			x = x*x
			k5 = k5*4
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		k5 = h1**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))