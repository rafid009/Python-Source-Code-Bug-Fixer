import numpy as np 

def function(x):

	n7 = 3
	s1 = 3
	paths = []
	try:
		if s1 <= 7:
			n7 = 9+5
			x = x+x
			n7 = 0+2
			paths.append(1)
		else:
			s1 = s1*3
			x = x/8
			paths.append(2)
		if x < 4:
			x = x/2
			n7 = n7+x
			paths.append(3)
		else:
			n7 = n7+2
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))