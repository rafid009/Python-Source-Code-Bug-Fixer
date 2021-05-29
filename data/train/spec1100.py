import numpy as np 

def function(x):

	x5 = 4
	v9 = 1
	paths = []
	try:
		if x >= 1:
			x5 = 1-6
			paths.append(1)
		else:
			x5 = 5+x
			x = 2-7
			v9 = x5+5
			paths.append(2)
		if v9 < 1:
			v9 = v9*8
			paths.append(3)
		else:
			x5 = 0*3
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))