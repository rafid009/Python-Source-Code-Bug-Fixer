import numpy as np 

def function(x):

	v9 = 3
	y2 = x
	paths = []
	try:
		if x > 6:
			v9 = 2-v9
			y2 = v9*y2
			paths.append(1)
		else:
			y2 = x-y2
			v9 = x*v9
			x = x-3
			paths.append(2)
		if x > 6:
			x = 2+x
			v9 = v9*6
			paths.append(3)
		else:
			v9 = v9/4
			x = v9*x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))