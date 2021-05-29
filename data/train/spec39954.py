import numpy as np 

def function(x):

	m7 = x
	p0 = 2
	paths = []
	try:
		if p0 < 6:
			x = x*8
			paths.append(1)
		else:
			p0 = 4/p0
			p0 = p0/m7
			paths.append(2)
		if x > 9:
			x = x+8
			m7 = m7-1
			x = 7+x
			paths.append(3)
		else:
			p0 = m7-x
			x = x-p0
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