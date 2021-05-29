import numpy as np 

def function(x):

	m8 = 6
	s1 = 1
	paths = []
	try:
		if x > 5:
			s1 = s1+m8
			paths.append(1)
		else:
			m8 = s1/3
			x = m8*6
			m8 = 6/5
			paths.append(2)
		if s1 > 7:
			m8 = m8+7
			x = s1/3
			m8 = m8/7
			paths.append(3)
		else:
			x = s1-2
			m8 = m8-1
			m8 = s1+m8
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