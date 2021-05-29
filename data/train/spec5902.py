import numpy as np 

def function(x):

	k5 = x
	f1 = 0
	paths = []
	try:
		if f1 >= 7:
			f1 = x-k5
			f1 = f1-8
			f1 = f1/x
			paths.append(1)
		else:
			x = 4*2
			x = 6-9
			f1 = 7-k5
			paths.append(2)
		if f1 < 3:
			k5 = k5/7
			k5 = x+f1
			paths.append(3)
		else:
			k5 = 9+5
			f1 = 7+f1
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