import numpy as np 

def function(x):

	s2 = x
	m4 = 8
	paths = []
	try:
		if x <= 2:
			m4 = m4/x
			paths.append(1)
		else:
			s2 = s2+m4
			x = 8*x
			s2 = m4/s2
			paths.append(2)
		if s2 > 7:
			m4 = 9+m4
			x = 4*x
			paths.append(3)
		else:
			m4 = 2*2
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))