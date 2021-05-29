import numpy as np 

def function(x):

	s2 = 1
	m9 = x
	paths = []
	try:
		if s2 > 4:
			m9 = s2+7
			m9 = 2-0
			paths.append(1)
		else:
			x = x/7
			s2 = m9+1
			paths.append(2)
		if m9 > 3:
			m9 = m9/m9
			paths.append(3)
		else:
			s2 = x-s2
			m9 = s2-0
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))