import numpy as np 

def function(x):

	b5 = 2
	j4 = x
	x = 3
	paths = []
	try:
		if b5 <= 5:
			x = x-2
			x = x-x
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if j4 <= 6:
			b5 = 0*b5
			paths.append(3)
		else:
			b5 = 5*4
			b5 = 5*6
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))