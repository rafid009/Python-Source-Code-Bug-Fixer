import numpy as np 

def function(x):

	s8 = x
	n6 = x
	paths = []
	try:
		if x <= 1:
			s8 = n6+7
			x = 3+s8
			paths.append(1)
		else:
			x = x+x
			x = x*6
			x = 1+3
			paths.append(2)
		if n6 > 7:
			s8 = s8-1
			paths.append(3)
		else:
			n6 = x/n6
			s8 = 1*x
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