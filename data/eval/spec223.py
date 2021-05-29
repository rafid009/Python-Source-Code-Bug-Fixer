import numpy as np 

def function(x):

	i9 = 4
	f3 = x
	paths = []
	try:
		if x <= 3:
			i9 = f3/x
			x = 9+x
			i9 = 6*x
			paths.append(1)
		else:
			f3 = 4+f3
			f3 = f3+6
			x = 6-8
			paths.append(2)
		if f3 > 3:
			f3 = i9/5
			paths.append(3)
		else:
			f3 = f3*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))