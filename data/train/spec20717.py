import numpy as np 

def function(x):

	s9 = 8
	b2 = 7
	paths = []
	try:
		if b2 < 2:
			s9 = s9-s9
			paths.append(1)
		else:
			b2 = 1/x
			b2 = 7+b2
			paths.append(2)
		if b2 <= 5:
			x = 2+1
			paths.append(3)
		else:
			b2 = 0-x
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))