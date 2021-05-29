import numpy as np 

def function(x):

	h1 = x
	k7 = x
	paths = []
	try:
		if x > 8:
			k7 = k7-h1
			paths.append(1)
		else:
			k7 = k7+h1
			h1 = 8*h1
			k7 = 3*h1
			paths.append(2)
		if x > 3:
			x = h1/3
			x = k7/h1
			k7 = 0*k7
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		k7 = h1**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))