import numpy as np 

def function(x):

	g5 = 4
	b9 = x
	x = 5
	paths = []
	try:
		if x > 7:
			x = x/g5
			paths.append(1)
		else:
			g5 = 1/g5
			g5 = 0-g5
			b9 = b9-6
			paths.append(2)
		if x > 6:
			g5 = g5-8
			x = 2*x
			paths.append(3)
		else:
			x = 4-9
			b9 = b9-1
			x = x+8
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		b9 = g5**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))