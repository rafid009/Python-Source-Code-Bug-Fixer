import numpy as np 

def function(x):

	h7 = x
	b3 = 8
	paths = []
	try:
		if x <= 1:
			x = x-8
			paths.append(1)
		else:
			x = x+b3
			x = 8+x
			paths.append(2)
		if h7 <= 7:
			x = x/8
			paths.append(3)
		else:
			x = h7/x
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		b3 = h7**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))