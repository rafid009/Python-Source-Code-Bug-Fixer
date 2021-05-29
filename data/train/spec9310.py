import numpy as np 

def function(x):

	y9 = x
	f5 = 5
	x = 8
	paths = []
	try:
		if x > 6:
			x = 6*5
			paths.append(1)
		else:
			f5 = f5-3
			f5 = f5*1
			paths.append(2)
		if y9 < 8:
			x = x/f5
			y9 = y9*3
			paths.append(3)
		else:
			x = f5*x
			x = x-3
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		f5 = y9**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))