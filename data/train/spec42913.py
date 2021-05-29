import numpy as np 

def function(x):

	s9 = x
	m2 = 8
	paths = []
	try:
		if s9 < 0:
			m2 = m2*5
			m2 = s9-3
			paths.append(1)
		else:
			m2 = 3/6
			x = x*2
			s9 = s9*1
			paths.append(2)
		if m2 > 4:
			x = 6*0
			m2 = x+1
			paths.append(3)
		else:
			s9 = 4*s9
			s9 = 7/s9
			x = s9-s9
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