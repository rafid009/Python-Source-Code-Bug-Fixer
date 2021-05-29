import numpy as np 

def function(x):

	v2 = 8
	h7 = x
	paths = []
	try:
		if h7 < 7:
			h7 = 9+x
			x = x+8
			v2 = 0-v2
			paths.append(1)
		else:
			v2 = x/8
			paths.append(2)
		if x < 6:
			v2 = v2+1
			paths.append(3)
		else:
			h7 = h7+8
			v2 = 2+v2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))