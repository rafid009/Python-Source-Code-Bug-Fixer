import numpy as np 

def function(x):

	b3 = 1
	s9 = 2
	paths = []
	try:
		if b3 > 4:
			b3 = 5/7
			x = x*6
			s9 = 8+s9
			paths.append(1)
		else:
			s9 = s9*4
			paths.append(2)
		if b3 >= 3:
			x = 9+x
			b3 = 8-8
			paths.append(3)
		else:
			s9 = b3/s9
			b3 = x-4
			x = 4+9
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))