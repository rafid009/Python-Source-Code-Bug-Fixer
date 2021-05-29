import numpy as np 

def function(x):

	h7 = x
	y6 = 0
	paths = []
	try:
		if h7 <= 3:
			y6 = 6+1
			y6 = y6-9
			x = 2+x
			paths.append(1)
		else:
			x = 6-9
			y6 = x+h7
			h7 = 8*0
			paths.append(2)
		if x >= 4:
			x = 2+x
			x = 1-x
			x = x-0
			paths.append(3)
		else:
			x = 9+h7
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))