import numpy as np 

def function(x):

	s4 = 2
	m4 = 0
	paths = []
	try:
		if x >= 6:
			x = 5*5
			x = x+9
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if s4 < 7:
			m4 = 8+0
			m4 = 4+x
			paths.append(3)
		else:
			m4 = 2/7
			x = x-4
			x = x+4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		s4 = m4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))