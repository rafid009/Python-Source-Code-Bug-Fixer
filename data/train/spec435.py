import numpy as np 

def function(x):

	b4 = 1
	r4 = x
	x = x
	paths = []
	try:
		if x < 1:
			b4 = 5-b4
			paths.append(1)
		else:
			r4 = r4/4
			paths.append(2)
		if b4 > 4:
			x = 9-x
			x = 2*x
			r4 = 6+r4
			paths.append(3)
		else:
			b4 = 1-1
			x = x-9
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))