import numpy as np 

def function(x):

	m4 = x
	s8 = 9
	paths = []
	try:
		if m4 < 7:
			x = x-6
			paths.append(1)
		else:
			m4 = 7/8
			m4 = m4+9
			x = x*5
			paths.append(2)
		if m4 > 0:
			x = 7/6
			x = x/s8
			m4 = 4/m4
			paths.append(3)
		else:
			x = x/6
			m4 = m4+s8
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		s8 = m4**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))