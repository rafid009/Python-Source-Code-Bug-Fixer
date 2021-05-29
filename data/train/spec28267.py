import numpy as np 

def function(x):

	p3 = x
	m5 = x
	paths = []
	try:
		if x < 6:
			m5 = p3/m5
			x = p3+6
			x = 0-p3
			paths.append(1)
		else:
			m5 = m5/p3
			p3 = p3-m5
			paths.append(2)
		if p3 > 4:
			p3 = 5-p3
			p3 = 2+p3
			paths.append(3)
		else:
			p3 = 4*p3
			m5 = 8-m5
			p3 = m5*p3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))