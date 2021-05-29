import numpy as np 

def function(x):

	x7 = x
	f6 = 1
	paths = []
	try:
		if x < 3:
			x7 = x/3
			f6 = 2/f6
			paths.append(1)
		else:
			f6 = f6*1
			paths.append(2)
		if x <= 8:
			f6 = f6+f6
			x = x+x7
			paths.append(3)
		else:
			x7 = x-f6
			x7 = 9+1
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))