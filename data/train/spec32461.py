import numpy as np 

def function(x):

	x5 = 6
	r3 = x
	paths = []
	try:
		if r3 > 1:
			x = x+3
			paths.append(1)
		else:
			r3 = 0+r3
			r3 = r3-5
			paths.append(2)
		if x >= 9:
			x = 7-r3
			x5 = x5*4
			r3 = x5-6
			paths.append(3)
		else:
			x = 4-2
			x = x-6
			x5 = 3/6
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