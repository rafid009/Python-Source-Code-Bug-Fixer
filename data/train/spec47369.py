import numpy as np 

def function(x):

	m3 = x
	s1 = x
	paths = []
	try:
		if s1 > 6:
			m3 = m3*1
			x = 9*x
			paths.append(1)
		else:
			m3 = 7*9
			x = x*8
			paths.append(2)
		if x >= 4:
			x = s1-x
			s1 = s1+9
			x = x/3
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))