import numpy as np 

def function(x):

	m5 = x
	p7 = x
	x = x
	paths = []
	try:
		if m5 < 9:
			m5 = m5+8
			m5 = m5-5
			p7 = p7-x
			paths.append(1)
		else:
			x = 9*7
			m5 = 6-0
			paths.append(2)
		if x >= 3:
			x = x/6
			p7 = 0*p7
			p7 = p7+x
			paths.append(3)
		else:
			p7 = 3*x
			x = 2+4
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		m5 = p7**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))