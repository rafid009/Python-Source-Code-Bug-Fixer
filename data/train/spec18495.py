import numpy as np 

def function(x):

	m0 = 0
	r3 = 1
	paths = []
	try:
		if m0 < 2:
			x = m0-4
			m0 = m0-6
			paths.append(1)
		else:
			x = x-r3
			m0 = m0-r3
			x = x+7
			paths.append(2)
		if r3 > 0:
			r3 = m0/6
			paths.append(3)
		else:
			r3 = r3+r3
			x = 9-x
			m0 = 4+m0
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		m0 = r3**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))