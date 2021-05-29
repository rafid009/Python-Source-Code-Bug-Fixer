import numpy as np 

def function(x):

	y2 = x
	a3 = 0
	paths = []
	try:
		if x >= 7:
			a3 = 5-y2
			paths.append(1)
		else:
			a3 = 8-a3
			paths.append(2)
		if x < 0:
			a3 = x+a3
			x = 6/x
			a3 = a3*0
			paths.append(3)
		else:
			x = x/2
			x = a3+8
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		y2 = a3**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))