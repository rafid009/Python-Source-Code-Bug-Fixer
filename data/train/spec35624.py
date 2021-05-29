import numpy as np 

def function(x):

	s5 = 2
	m8 = 8
	paths = []
	try:
		if x <= 7:
			m8 = m8/m8
			x = x+0
			paths.append(1)
		else:
			s5 = 0*s5
			x = s5+x
			m8 = 3+x
			paths.append(2)
		if s5 <= 7:
			m8 = x-s5
			paths.append(3)
		else:
			x = m8-8
			s5 = s5+s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))