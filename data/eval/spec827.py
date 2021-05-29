import numpy as np 

def function(x):

	v1 = x
	h8 = 1
	paths = []
	try:
		if v1 >= 8:
			h8 = v1+9
			paths.append(1)
		else:
			h8 = 6-h8
			h8 = x/5
			x = x*h8
			paths.append(2)
		if h8 <= 8:
			h8 = v1*4
			h8 = x/h8
			h8 = h8+h8
			paths.append(3)
		else:
			x = h8+x
			h8 = 6+5
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		v1 = h8**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))