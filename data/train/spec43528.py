import numpy as np 

def function(x):

	m2 = 9
	s1 = 0
	paths = []
	try:
		if s1 > 3:
			m2 = 7+m2
			s1 = s1*2
			x = x/4
			paths.append(1)
		else:
			s1 = 8*7
			paths.append(2)
		if m2 > 6:
			x = 2-5
			paths.append(3)
		else:
			m2 = m2-3
			s1 = 0+s1
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