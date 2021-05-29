import numpy as np 

def function(x):

	y2 = 4
	t3 = x
	paths = []
	try:
		if y2 >= 5:
			y2 = 9/5
			y2 = y2/x
			paths.append(1)
		else:
			x = x+x
			x = 3/8
			paths.append(2)
		if x > 8:
			y2 = x+t3
			paths.append(3)
		else:
			x = 3*x
			x = x+8
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))