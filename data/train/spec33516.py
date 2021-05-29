import numpy as np 

def function(x):

	f8 = x
	q4 = 0
	paths = []
	try:
		if x >= 3:
			q4 = f8+f8
			paths.append(1)
		else:
			q4 = 4*7
			paths.append(2)
		if f8 <= 9:
			q4 = 4-q4
			q4 = 6/q4
			paths.append(3)
		else:
			q4 = f8*q4
			x = x/6
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))