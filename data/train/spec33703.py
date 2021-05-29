import numpy as np 

def function(x):

	u1 = 5
	h1 = 2
	paths = []
	try:
		if u1 <= 6:
			x = 7+x
			paths.append(1)
		else:
			h1 = 2+h1
			x = x-u1
			h1 = h1/7
			paths.append(2)
		if x < 0:
			u1 = x+x
			x = x-x
			paths.append(3)
		else:
			h1 = x/x
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))