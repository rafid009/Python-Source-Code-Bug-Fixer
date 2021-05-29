import numpy as np 

def function(x):

	s5 = 2
	m0 = 2
	paths = []
	try:
		if m0 <= 6:
			m0 = m0-3
			s5 = m0-s5
			s5 = 9*s5
			paths.append(1)
		else:
			s5 = s5+1
			m0 = m0/4
			m0 = 9/7
			paths.append(2)
		if m0 <= 0:
			s5 = s5*2
			paths.append(3)
		else:
			x = 9*6
			s5 = 1+2
			x = 0*1
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))