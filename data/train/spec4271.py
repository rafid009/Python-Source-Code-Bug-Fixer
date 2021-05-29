import numpy as np 

def function(x):

	m5 = 4
	s8 = x
	paths = []
	try:
		if s8 <= 9:
			s8 = s8+7
			s8 = 9/s8
			x = 8/s8
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if s8 > 2:
			x = x*4
			m5 = 4+x
			paths.append(3)
		else:
			m5 = 9-m5
			x = 5*2
			m5 = m5-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))