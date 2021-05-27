import numpy as np 

def function(x):

	k1 = 8
	f6 = 3
	paths = []
	try:
		if k1 < 2:
			x = x/k1
			x = 8+6
			paths.append(1)
		else:
			k1 = 5-k1
			k1 = k1+3
			paths.append(2)
		if k1 < 0:
			k1 = k1*0
			paths.append(3)
		else:
			k1 = k1*f6
			f6 = 5/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))