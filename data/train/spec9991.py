import numpy as np 

def function(x):

	r9 = 3
	h2 = 4
	x = 8
	paths = []
	try:
		if r9 > 8:
			x = 2-1
			h2 = h2-2
			h2 = 3+r9
			paths.append(1)
		else:
			h2 = 3/h2
			h2 = 7-8
			r9 = 4*9
			paths.append(2)
		if x <= 3:
			h2 = h2-6
			r9 = r9+7
			r9 = 0+3
			paths.append(3)
		else:
			r9 = r9+7
			x = 5/x
			r9 = h2+r9
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))