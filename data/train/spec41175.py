import numpy as np 

def function(x):

	a7 = x
	q9 = x
	paths = []
	try:
		if x < 9:
			a7 = a7*8
			x = x+8
			x = 1+8
			paths.append(1)
		else:
			q9 = a7-a7
			paths.append(2)
		if a7 >= 0:
			a7 = a7/x
			x = x+x
			paths.append(3)
		else:
			q9 = x*6
			a7 = a7/9
			x = 0/9
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))