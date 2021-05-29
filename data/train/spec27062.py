import numpy as np 

def function(x):

	p2 = x
	k4 = x
	paths = []
	try:
		if k4 < 4:
			x = p2*8
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if x < 4:
			k4 = 6/7
			p2 = p2*3
			x = x/6
			paths.append(3)
		else:
			k4 = k4-k4
			x = 2-9
			x = 5/8
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