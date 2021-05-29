import numpy as np 

def function(x):

	j4 = 1
	b5 = x
	x = x
	paths = []
	try:
		if x > 6:
			j4 = 2-3
			paths.append(1)
		else:
			j4 = 2+j4
			paths.append(2)
		if b5 >= 3:
			b5 = 1-b5
			paths.append(3)
		else:
			b5 = 0+9
			x = 2+5
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