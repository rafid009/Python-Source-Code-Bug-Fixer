import numpy as np 

def function(x):

	n9 = x
	y2 = 0
	paths = []
	try:
		if x > 6:
			x = x+7
			paths.append(1)
		else:
			x = n9+5
			x = x-n9
			paths.append(2)
		if y2 <= 9:
			y2 = n9-9
			x = n9-0
			n9 = 7/n9
			paths.append(3)
		else:
			x = x+x
			n9 = 8+6
			x = x+0
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))