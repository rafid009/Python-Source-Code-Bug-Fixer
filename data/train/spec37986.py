import numpy as np 

def function(x):

	p0 = x
	m6 = x
	x = x
	paths = []
	try:
		if m6 <= 1:
			p0 = p0+9
			x = 2*x
			paths.append(1)
		else:
			m6 = m6*1
			p0 = p0*4
			x = 7*p0
			paths.append(2)
		if x > 0:
			m6 = m6/4
			paths.append(3)
		else:
			p0 = 1-p0
			x = x*8
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		p0 = m6**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))