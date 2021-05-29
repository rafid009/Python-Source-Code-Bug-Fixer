import numpy as np 

def function(x):

	b4 = 2
	s9 = 0
	x = 7
	paths = []
	try:
		if b4 >= 6:
			x = x+s9
			s9 = s9+9
			paths.append(1)
		else:
			x = x+s9
			s9 = 7+s9
			paths.append(2)
		if x > 8:
			s9 = s9/3
			x = x+4
			paths.append(3)
		else:
			s9 = s9/3
			b4 = 2*4
			s9 = s9-9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))