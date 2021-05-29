import numpy as np 

def function(x):

	s1 = x
	m0 = x
	paths = []
	try:
		if m0 >= 0:
			x = x*4
			s1 = s1+s1
			m0 = x-m0
			paths.append(1)
		else:
			x = m0+m0
			s1 = s1/8
			s1 = 7/s1
			paths.append(2)
		if x <= 7:
			s1 = s1/8
			paths.append(3)
		else:
			m0 = m0/x
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