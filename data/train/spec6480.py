import numpy as np 

def function(x):

	x6 = x
	h7 = 8
	paths = []
	try:
		if x < 0:
			x6 = x-4
			x6 = 8+h7
			x6 = 0+x6
			paths.append(1)
		else:
			x6 = x6*3
			x6 = x+x6
			h7 = x6/h7
			paths.append(2)
		if x <= 5:
			x6 = x6/6
			x6 = x6*0
			paths.append(3)
		else:
			h7 = x-h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))