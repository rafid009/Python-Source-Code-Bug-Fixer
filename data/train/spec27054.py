import numpy as np 

def function(x):

	s6 = 8
	m5 = x
	paths = []
	try:
		if m5 > 1:
			x = x-m5
			x = 7+x
			paths.append(1)
		else:
			s6 = s6+m5
			x = m5-m5
			paths.append(2)
		if x <= 4:
			m5 = 2-8
			paths.append(3)
		else:
			x = 4-1
			m5 = s6/2
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))