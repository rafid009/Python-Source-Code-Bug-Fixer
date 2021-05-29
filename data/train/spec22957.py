import numpy as np 

def function(x):

	m7 = x
	s8 = 3
	paths = []
	try:
		if s8 < 0:
			m7 = s8*0
			s8 = s8*1
			x = s8-0
			paths.append(1)
		else:
			s8 = s8*x
			x = x+3
			x = x*0
			paths.append(2)
		if x >= 7:
			s8 = m7*m7
			s8 = 6+m7
			paths.append(3)
		else:
			m7 = m7-0
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		m7 = s8**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))