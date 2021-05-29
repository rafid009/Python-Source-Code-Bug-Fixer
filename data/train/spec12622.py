import numpy as np 

def function(x):

	p7 = 0
	m6 = 4
	paths = []
	try:
		if x > 7:
			x = x*m6
			x = x+m6
			x = 7+p7
			paths.append(1)
		else:
			m6 = m6-x
			p7 = 1/4
			paths.append(2)
		if p7 < 4:
			x = x-m6
			x = x+m6
			p7 = 7-8
			paths.append(3)
		else:
			m6 = 9+m6
			m6 = m6-5
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))