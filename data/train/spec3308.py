import numpy as np 

def function(x):

	j0 = x
	y3 = x
	paths = []
	try:
		if x < 9:
			y3 = y3/8
			paths.append(1)
		else:
			j0 = 3+0
			j0 = 4*0
			paths.append(2)
		if x > 4:
			x = 7/x
			paths.append(3)
		else:
			x = x/9
			y3 = 9*j0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))