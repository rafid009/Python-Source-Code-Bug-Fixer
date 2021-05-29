import numpy as np 

def function(x):

	m1 = 4
	s1 = x
	paths = []
	try:
		if m1 <= 9:
			m1 = 5/m1
			m1 = x*x
			x = x*6
			paths.append(1)
		else:
			m1 = m1+9
			x = 0+1
			s1 = s1+7
			paths.append(2)
		if s1 > 3:
			m1 = m1/x
			s1 = s1-3
			paths.append(3)
		else:
			x = x/3
			s1 = s1*3
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		m1 = s1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))