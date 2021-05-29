import numpy as np 

def function(x):

	s5 = 4
	m3 = 4
	paths = []
	try:
		if s5 < 4:
			m3 = m3-m3
			x = 9-4
			paths.append(1)
		else:
			m3 = m3-7
			s5 = x-1
			s5 = x*5
			paths.append(2)
		if s5 < 6:
			m3 = m3*2
			x = 5*x
			paths.append(3)
		else:
			s5 = s5/m3
			x = 0*8
			s5 = s5+s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		m3 = s5**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))