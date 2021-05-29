import numpy as np 

def function(x):

	u3 = x
	h0 = 8
	paths = []
	try:
		if u3 > 8:
			x = u3*8
			x = u3+9
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if u3 <= 1:
			h0 = 8/h0
			x = x-x
			paths.append(3)
		else:
			u3 = 6*u3
			u3 = 8/x
			x = x-h0
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))