import numpy as np 

def function(x):

	p0 = x
	m9 = x
	paths = []
	try:
		if m9 < 6:
			p0 = p0-m9
			paths.append(1)
		else:
			m9 = m9/p0
			x = p0/x
			p0 = 3+x
			paths.append(2)
		if m9 <= 6:
			p0 = m9/5
			p0 = m9*p0
			p0 = p0+6
			paths.append(3)
		else:
			p0 = p0+p0
			x = 1/9
			p0 = 4+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))