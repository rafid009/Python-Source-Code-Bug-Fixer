import numpy as np 

def function(x):

	v1 = x
	h8 = 9
	paths = []
	try:
		if v1 < 3:
			x = 7/h8
			x = 0+2
			h8 = h8+3
			paths.append(1)
		else:
			v1 = 3-8
			paths.append(2)
		if v1 < 3:
			x = h8+x
			paths.append(3)
		else:
			x = x+h8
			v1 = v1+2
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))