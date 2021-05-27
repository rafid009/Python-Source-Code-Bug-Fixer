import numpy as np 

def function(x):

	p7 = 4
	m0 = 7
	paths = []
	try:
		if m0 <= 1:
			m0 = m0+9
			m0 = m0-0
			paths.append(1)
		else:
			m0 = m0-x
			x = x+4
			m0 = x+8
			paths.append(2)
		if p7 >= 5:
			m0 = 5-m0
			x = p7*p7
			x = 2/7
			paths.append(3)
		else:
			p7 = x/1
			x = x+p7
			m0 = p7-m0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))