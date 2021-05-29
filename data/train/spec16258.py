import numpy as np 

def function(x):

	t7 = 3
	m0 = 4
	paths = []
	try:
		if m0 > 5:
			m0 = m0/8
			paths.append(1)
		else:
			t7 = t7-6
			m0 = m0-8
			x = x/1
			paths.append(2)
		if t7 <= 8:
			x = m0*x
			paths.append(3)
		else:
			m0 = m0-3
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))