import numpy as np 

def function(x):

	s5 = x
	m5 = x
	paths = []
	try:
		if s5 < 3:
			x = x/8
			m5 = 4*m5
			paths.append(1)
		else:
			x = 2*3
			x = x-6
			s5 = s5-0
			paths.append(2)
		if m5 >= 4:
			x = x-5
			m5 = m5-s5
			paths.append(3)
		else:
			m5 = m5+9
			x = 6*1
			s5 = 1*s5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))