import numpy as np 

def function(x):

	p2 = 0
	m2 = x
	paths = []
	try:
		if x <= 7:
			m2 = m2*8
			x = 4+x
			paths.append(1)
		else:
			p2 = 2+p2
			p2 = p2/1
			paths.append(2)
		if p2 > 8:
			p2 = 6+p2
			x = x+4
			paths.append(3)
		else:
			p2 = p2/6
			p2 = p2*p2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))