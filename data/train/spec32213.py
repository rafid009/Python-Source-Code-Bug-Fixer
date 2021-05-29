import numpy as np 

def function(x):

	v7 = 6
	f5 = 2
	paths = []
	try:
		if v7 <= 6:
			f5 = 3*4
			v7 = 1-v7
			paths.append(1)
		else:
			v7 = 8*8
			x = x*6
			paths.append(2)
		if v7 > 8:
			x = 6-f5
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))