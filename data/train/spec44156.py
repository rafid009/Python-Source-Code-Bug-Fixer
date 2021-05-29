import numpy as np 

def function(x):

	x4 = x
	p2 = x
	paths = []
	try:
		if x4 < 6:
			x = x-4
			x4 = x/x4
			p2 = 8*p2
			paths.append(1)
		else:
			p2 = 4+5
			x4 = x4/9
			paths.append(2)
		if p2 >= 7:
			x4 = 8+8
			p2 = 0-6
			paths.append(3)
		else:
			x = x+7
			x = 5-p2
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