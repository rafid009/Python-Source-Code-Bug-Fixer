import numpy as np 

def function(x):

	s7 = 3
	m2 = 2
	paths = []
	try:
		if x < 5:
			m2 = 3+m2
			x = x-7
			paths.append(1)
		else:
			s7 = s7-5
			paths.append(2)
		if x < 7:
			x = 1/x
			x = x+x
			paths.append(3)
		else:
			m2 = m2/m2
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		m2 = s7**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))