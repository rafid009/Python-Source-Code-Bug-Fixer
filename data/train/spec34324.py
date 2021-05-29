import numpy as np 

def function(x):

	k6 = 9
	y2 = x
	paths = []
	try:
		if x >= 2:
			y2 = y2/6
			y2 = y2+8
			k6 = y2-k6
			paths.append(1)
		else:
			x = y2/9
			x = x+x
			paths.append(2)
		if k6 > 2:
			y2 = y2+2
			paths.append(3)
		else:
			x = y2*y2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))