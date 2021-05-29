import numpy as np 

def function(x):

	v5 = x
	h8 = 2
	paths = []
	try:
		if v5 < 6:
			h8 = 1*0
			h8 = x+h8
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if h8 >= 4:
			x = 7/h8
			x = 2+h8
			x = h8+2
			paths.append(3)
		else:
			v5 = 4+v5
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))