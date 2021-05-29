import numpy as np 

def function(x):

	n5 = 4
	b9 = x
	x = 8
	paths = []
	try:
		if n5 > 8:
			x = 9*6
			x = 6*x
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if n5 < 4:
			x = x/1
			paths.append(3)
		else:
			x = 3*9
			x = 7*6
			n5 = 6/n5
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))