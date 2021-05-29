import numpy as np 

def function(x):

	f5 = 2
	y9 = x
	paths = []
	try:
		if y9 <= 3:
			y9 = y9/f5
			x = 1/x
			x = x-0
			paths.append(1)
		else:
			y9 = y9/7
			f5 = 5-f5
			f5 = f5-4
			paths.append(2)
		if x > 3:
			x = 4/x
			x = x+f5
			y9 = y9/1
			paths.append(3)
		else:
			y9 = 1*3
			f5 = 9*5
			y9 = 8+y9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))