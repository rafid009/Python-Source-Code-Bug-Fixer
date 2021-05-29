import numpy as np 

def function(x):

	s1 = 2
	m1 = x
	paths = []
	try:
		if m1 < 2:
			s1 = s1+s1
			x = x-2
			m1 = m1*6
			paths.append(1)
		else:
			x = m1/x
			paths.append(2)
		if m1 > 2:
			s1 = m1+x
			x = x*m1
			m1 = x+m1
			paths.append(3)
		else:
			s1 = 3-s1
			s1 = 5-7
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))