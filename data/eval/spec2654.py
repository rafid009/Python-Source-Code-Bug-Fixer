import numpy as np 

def function(x):

	h7 = x
	x6 = x
	paths = []
	try:
		if x <= 9:
			x6 = x6/8
			x = x6-1
			x = 9+x
			paths.append(1)
		else:
			x6 = 1*x6
			x = x6*2
			paths.append(2)
		if x > 2:
			x6 = 2+x6
			paths.append(3)
		else:
			h7 = x+3
			h7 = 1*8
			h7 = 0+x
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x6 = h7**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))