import numpy as np 

def function(x):

	a8 = 6
	n7 = 7
	paths = []
	try:
		if n7 <= 0:
			x = x+a8
			paths.append(1)
		else:
			n7 = n7-3
			x = 8*x
			paths.append(2)
		if n7 > 0:
			x = x/2
			a8 = x/a8
			paths.append(3)
		else:
			n7 = n7-8
			n7 = n7+x
			n7 = n7-6
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))