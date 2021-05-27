import numpy as np 

def function(x):

	n1 = x
	y1 = x
	paths = []
	try:
		if n1 < 5:
			y1 = y1*5
			paths.append(1)
		else:
			y1 = 2-0
			paths.append(2)
		if y1 <= 4:
			x = y1-y1
			x = x+2
			paths.append(3)
		else:
			x = n1/8
			n1 = n1-6
			n1 = 3-n1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))