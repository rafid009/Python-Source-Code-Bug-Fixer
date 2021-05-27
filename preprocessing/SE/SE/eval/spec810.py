import numpy as np 

def function(x):

	m2 = x
	p7 = 6
	x = 8
	paths = []
	try:
		if m2 <= 7:
			p7 = 3+6
			m2 = 3*p7
			paths.append(1)
		else:
			x = x*x
			p7 = p7-m2
			paths.append(2)
		if p7 <= 2:
			m2 = 7/m2
			paths.append(3)
		else:
			m2 = 5-m2
			m2 = m2/x
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))