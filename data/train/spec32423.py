import numpy as np 

def function(x):

	y9 = x
	s1 = 0
	paths = []
	try:
		if s1 <= 5:
			s1 = s1*2
			x = x-5
			s1 = s1/1
			paths.append(1)
		else:
			s1 = x-9
			paths.append(2)
		if y9 >= 7:
			y9 = s1/7
			s1 = 6+s1
			s1 = s1+6
			paths.append(3)
		else:
			s1 = s1-x
			x = 6-s1
			s1 = s1/9
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