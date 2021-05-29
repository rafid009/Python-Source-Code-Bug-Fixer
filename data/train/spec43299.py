import numpy as np 

def function(x):

	s4 = 8
	m5 = x
	paths = []
	try:
		if x <= 1:
			m5 = 0+m5
			m5 = 9-1
			m5 = 8/m5
			paths.append(1)
		else:
			m5 = x*5
			paths.append(2)
		if x > 9:
			x = x+0
			paths.append(3)
		else:
			s4 = m5/7
			x = 6+x
			s4 = m5-5
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))