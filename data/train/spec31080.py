import numpy as np 

def function(x):

	b9 = 8
	x2 = 4
	paths = []
	try:
		if x2 < 6:
			b9 = x2+b9
			x = 6-2
			paths.append(1)
		else:
			x2 = 4/8
			x = 0*x2
			paths.append(2)
		if x2 >= 9:
			b9 = b9+4
			x = x*3
			x2 = x/x
			paths.append(3)
		else:
			b9 = 7-b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x2 = b9**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))