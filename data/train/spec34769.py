import numpy as np 

def function(x):

	f2 = x
	y9 = x
	paths = []
	try:
		if y9 > 5:
			x = 8/x
			paths.append(1)
		else:
			x = y9-x
			f2 = 4+x
			x = x+y9
			paths.append(2)
		if y9 > 0:
			y9 = 0-7
			f2 = f2/1
			f2 = 7-f2
			paths.append(3)
		else:
			x = x*5
			y9 = y9-x
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		f2 = y9**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))