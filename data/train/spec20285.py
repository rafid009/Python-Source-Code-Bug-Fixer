import numpy as np 

def function(x):

	m2 = 7
	s1 = x
	paths = []
	try:
		if x < 3:
			m2 = 0-s1
			s1 = 7/s1
			paths.append(1)
		else:
			m2 = 4+m2
			paths.append(2)
		if s1 <= 5:
			x = x*x
			paths.append(3)
		else:
			x = m2-0
			x = s1+x
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