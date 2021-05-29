import numpy as np 

def function(x):

	m7 = 5
	v6 = x
	paths = []
	try:
		if x <= 2:
			m7 = m7-8
			m7 = v6-m7
			paths.append(1)
		else:
			x = 3-x
			v6 = v6+m7
			paths.append(2)
		if v6 <= 7:
			m7 = m7/2
			x = 3+5
			paths.append(3)
		else:
			v6 = x-m7
			v6 = 4*v6
			m7 = m7*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))