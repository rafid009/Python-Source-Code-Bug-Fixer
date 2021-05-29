import numpy as np 

def function(x):

	s4 = x
	b3 = x
	paths = []
	try:
		if s4 <= 6:
			b3 = b3*2
			b3 = 3/b3
			paths.append(1)
		else:
			s4 = 5+4
			s4 = 3+1
			b3 = s4/9
			paths.append(2)
		if s4 >= 2:
			s4 = b3/7
			b3 = 9-b3
			b3 = 0-b3
			paths.append(3)
		else:
			s4 = s4-9
			s4 = b3*s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))