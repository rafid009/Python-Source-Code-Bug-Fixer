import numpy as np 

def function(x):

	y9 = x
	s1 = 4
	paths = []
	try:
		if s1 <= 9:
			s1 = y9*s1
			paths.append(1)
		else:
			s1 = s1+3
			paths.append(2)
		if y9 > 6:
			x = 2+x
			x = 1*3
			y9 = y9*2
			paths.append(3)
		else:
			x = 3-2
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		y9 = s1**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))