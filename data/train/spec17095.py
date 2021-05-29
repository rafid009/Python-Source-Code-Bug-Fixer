import numpy as np 

def function(x):

	m2 = x
	p3 = x
	paths = []
	try:
		if m2 >= 3:
			x = 4*7
			paths.append(1)
		else:
			p3 = p3/m2
			m2 = m2+p3
			paths.append(2)
		if x >= 6:
			x = 9+4
			x = 0-5
			m2 = 0/p3
			paths.append(3)
		else:
			p3 = m2-p3
			p3 = m2/7
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))