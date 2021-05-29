import numpy as np 

def function(x):

	h6 = x
	f1 = x
	paths = []
	try:
		if h6 <= 6:
			f1 = h6+6
			paths.append(1)
		else:
			f1 = f1*2
			paths.append(2)
		if h6 > 2:
			x = 9+0
			h6 = h6/f1
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		h6 = f1**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))