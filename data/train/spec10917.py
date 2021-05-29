import numpy as np 

def function(x):

	h6 = 9
	r2 = 4
	paths = []
	try:
		if x > 8:
			r2 = r2-2
			r2 = r2-9
			h6 = h6+3
			paths.append(1)
		else:
			r2 = r2+r2
			paths.append(2)
		if x < 0:
			h6 = r2+h6
			x = h6/x
			h6 = h6+2
			paths.append(3)
		else:
			h6 = 8-h6
			x = x+x
			h6 = 5*1
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))