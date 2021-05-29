import numpy as np 

def function(x):

	m3 = x
	s1 = 8
	paths = []
	try:
		if m3 > 2:
			s1 = s1*3
			x = 0+x
			m3 = m3*4
			paths.append(1)
		else:
			x = x+2
			m3 = 5-6
			paths.append(2)
		if m3 < 5:
			s1 = x*s1
			paths.append(3)
		else:
			s1 = m3-s1
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))