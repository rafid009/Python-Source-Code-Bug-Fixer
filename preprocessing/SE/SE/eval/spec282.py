import numpy as np 

def function(x):

	m2 = 9
	s5 = 5
	paths = []
	try:
		if s5 <= 8:
			x = x/s5
			s5 = s5-3
			paths.append(1)
		else:
			x = 0+7
			s5 = s5+m2
			paths.append(2)
		if s5 > 8:
			s5 = s5+7
			s5 = 6/s5
			s5 = s5*6
			paths.append(3)
		else:
			m2 = m2/s5
			s5 = s5+x
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		m2 = s5**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))