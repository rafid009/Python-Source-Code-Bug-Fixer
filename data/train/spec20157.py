import numpy as np 

def function(x):

	s1 = 9
	k9 = 5
	paths = []
	try:
		if x < 1:
			x = 1*x
			paths.append(1)
		else:
			s1 = k9+0
			k9 = x/3
			k9 = s1-8
			paths.append(2)
		if x >= 6:
			k9 = 8*k9
			paths.append(3)
		else:
			s1 = k9*x
			k9 = k9*3
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))