import numpy as np 

def function(x):

	b8 = 8
	r3 = 8
	paths = []
	try:
		if x >= 4:
			r3 = x-r3
			x = 4*7
			paths.append(1)
		else:
			r3 = r3-3
			paths.append(2)
		if b8 <= 2:
			x = 9+6
			x = x/x
			r3 = x-r3
			paths.append(3)
		else:
			x = 1/7
			x = 5+9
			r3 = r3/9
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