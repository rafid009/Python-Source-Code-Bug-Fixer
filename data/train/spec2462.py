import numpy as np 

def function(x):

	k6 = x
	y2 = 8
	paths = []
	try:
		if y2 >= 6:
			y2 = y2/k6
			y2 = k6-y2
			y2 = 5-y2
			paths.append(1)
		else:
			y2 = x/2
			paths.append(2)
		if k6 < 6:
			y2 = y2-y2
			x = 8+x
			paths.append(3)
		else:
			y2 = y2*5
			x = x+0
			k6 = k6*4
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		k6 = y2**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))