import numpy as np 

def function(x):

	x4 = 0
	b9 = x
	paths = []
	try:
		if x4 > 2:
			x = 4/x4
			x4 = 5/8
			paths.append(1)
		else:
			x4 = 4+x4
			paths.append(2)
		if b9 > 8:
			x4 = 5*6
			x4 = x4/4
			x = 5/x
			paths.append(3)
		else:
			x = 0*b9
			x4 = x4+x4
			b9 = x4/b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x4 = b9**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))