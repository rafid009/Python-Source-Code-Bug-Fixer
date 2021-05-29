import numpy as np 

def function(x):

	m0 = x
	s9 = 1
	paths = []
	try:
		if m0 >= 1:
			m0 = m0*6
			s9 = s9-2
			paths.append(1)
		else:
			x = x*m0
			paths.append(2)
		if m0 < 4:
			s9 = m0+0
			x = x/4
			s9 = s9/m0
			paths.append(3)
		else:
			s9 = s9-8
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))