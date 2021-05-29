import numpy as np 

def function(x):

	l3 = 7
	y9 = 3
	paths = []
	try:
		if l3 < 4:
			l3 = l3-y9
			y9 = 4+9
			x = 8*x
			paths.append(1)
		else:
			x = x+2
			x = x-4
			x = x/4
			paths.append(2)
		if x > 9:
			l3 = 7-7
			l3 = 6+5
			y9 = 4+9
			paths.append(3)
		else:
			l3 = 7-l3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y9 = x**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))