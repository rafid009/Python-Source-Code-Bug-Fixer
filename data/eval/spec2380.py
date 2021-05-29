import numpy as np 

def function(x):

	s1 = 2
	n3 = x
	x = x
	paths = []
	try:
		if n3 < 6:
			x = 6*x
			n3 = s1/n3
			n3 = n3/x
			paths.append(1)
		else:
			n3 = s1/9
			n3 = n3+5
			n3 = x/n3
			paths.append(2)
		if n3 > 9:
			s1 = s1*x
			s1 = x/s1
			x = 9+4
			paths.append(3)
		else:
			n3 = 2/x
			x = 5-n3
			s1 = s1/6
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))