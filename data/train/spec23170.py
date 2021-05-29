import numpy as np 

def function(x):

	m5 = 9
	s2 = x
	paths = []
	try:
		if x <= 1:
			x = s2+x
			m5 = 7/5
			paths.append(1)
		else:
			m5 = m5/x
			x = 2*x
			x = 7*x
			paths.append(2)
		if m5 < 7:
			x = m5-x
			m5 = m5+9
			paths.append(3)
		else:
			s2 = s2-3
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))