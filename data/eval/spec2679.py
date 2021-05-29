import numpy as np 

def function(x):

	h5 = x
	u3 = 9
	paths = []
	try:
		if x <= 2:
			h5 = h5-7
			paths.append(1)
		else:
			x = 0/2
			h5 = x+2
			x = x+x
			paths.append(2)
		if u3 >= 5:
			x = 7+6
			u3 = u3/1
			x = 7*u3
			paths.append(3)
		else:
			u3 = 9/u3
			u3 = 3/u3
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		h5 = h5**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))