import numpy as np 

def function(x):

	t1 = x
	x4 = 8
	paths = []
	try:
		if t1 <= 3:
			t1 = t1-x
			x4 = x+x4
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if x <= 0:
			x4 = x4+x
			x = x-5
			x4 = x-x4
			paths.append(3)
		else:
			x4 = 9+3
			x4 = x4*7
			t1 = t1+1
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))