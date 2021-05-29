import numpy as np 

def function(x):

	b6 = x
	b8 = 7
	paths = []
	try:
		if b8 < 7:
			b6 = b6*3
			b6 = 4*b6
			paths.append(1)
		else:
			x = 7+x
			paths.append(2)
		if b6 <= 4:
			b8 = 7*b8
			paths.append(3)
		else:
			x = x/x
			b6 = 0/b6
			x = x/x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))