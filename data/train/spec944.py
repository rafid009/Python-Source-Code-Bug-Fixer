import numpy as np 

def function(x):

	s6 = 2
	m1 = x
	x = x
	paths = []
	try:
		if m1 <= 5:
			x = 6*x
			x = 3*x
			s6 = 3*6
			paths.append(1)
		else:
			x = x/x
			m1 = x*2
			paths.append(2)
		if s6 > 4:
			x = x-4
			paths.append(3)
		else:
			s6 = 0-3
			x = 3*0
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		s6 = m1**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))