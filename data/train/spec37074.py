import numpy as np 

def function(x):

	s1 = 9
	y9 = 1
	paths = []
	try:
		if s1 >= 2:
			s1 = s1+4
			s1 = 2+s1
			paths.append(1)
		else:
			s1 = s1/1
			y9 = 9*8
			s1 = s1-s1
			paths.append(2)
		if x < 7:
			y9 = y9+1
			x = x+s1
			y9 = y9+5
			paths.append(3)
		else:
			x = 2-x
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