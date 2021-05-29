import numpy as np 

def function(x):

	b5 = x
	s2 = x
	paths = []
	try:
		if b5 <= 7:
			b5 = x+0
			s2 = s2+2
			paths.append(1)
		else:
			s2 = s2+8
			x = 7+x
			b5 = s2-x
			paths.append(2)
		if b5 >= 7:
			b5 = 3/8
			s2 = s2-4
			paths.append(3)
		else:
			s2 = s2-b5
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))