import numpy as np 

def function(x):

	v6 = x
	m6 = x
	paths = []
	try:
		if m6 < 4:
			x = x*x
			x = x/x
			paths.append(1)
		else:
			m6 = m6-m6
			paths.append(2)
		if x >= 7:
			v6 = v6*8
			m6 = m6/7
			m6 = 9-m6
			paths.append(3)
		else:
			x = v6-8
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		m6 = v6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))