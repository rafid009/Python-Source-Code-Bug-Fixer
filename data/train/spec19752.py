import numpy as np 

def function(x):

	h7 = x
	u2 = x
	paths = []
	try:
		if u2 >= 9:
			u2 = u2*5
			u2 = h7+9
			paths.append(1)
		else:
			x = u2*1
			u2 = x+x
			u2 = u2+5
			paths.append(2)
		if h7 > 3:
			h7 = 9+h7
			x = 1/3
			paths.append(3)
		else:
			u2 = 0+u2
			u2 = 2*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))