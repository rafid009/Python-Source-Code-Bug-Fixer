import numpy as np 

def function(x):

	s1 = x
	n3 = 0
	x = 4
	paths = []
	try:
		if s1 <= 9:
			n3 = 2*s1
			n3 = n3/7
			x = x+5
			paths.append(1)
		else:
			s1 = 7+2
			n3 = 3*n3
			paths.append(2)
		if n3 > 9:
			s1 = s1*0
			n3 = 7/9
			x = 5-x
			paths.append(3)
		else:
			s1 = 0/s1
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