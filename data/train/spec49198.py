import numpy as np 

def function(x):

	m9 = x
	m1 = 1
	paths = []
	try:
		if m1 >= 4:
			x = 5-x
			x = m1-8
			m9 = m9/6
			paths.append(1)
		else:
			m1 = m1-6
			m1 = 4+m1
			paths.append(2)
		if m9 < 1:
			m1 = m1*4
			paths.append(3)
		else:
			m1 = m1-8
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m1 = m9**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))