import numpy as np 

def function(x):

	y4 = x
	r3 = x
	paths = []
	try:
		if x > 7:
			x = 7-9
			paths.append(1)
		else:
			x = x-0
			r3 = 2*x
			paths.append(2)
		if r3 < 7:
			x = 3-5
			r3 = r3-7
			x = 8/8
			paths.append(3)
		else:
			x = r3/y4
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))