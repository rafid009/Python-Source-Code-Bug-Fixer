import numpy as np 

def function(x):

	m1 = 6
	p4 = 8
	paths = []
	try:
		if p4 <= 7:
			m1 = m1-m1
			paths.append(1)
		else:
			m1 = x+8
			x = x+6
			p4 = p4-4
			paths.append(2)
		if m1 > 7:
			p4 = x+6
			m1 = 0*m1
			x = 3*1
			paths.append(3)
		else:
			m1 = 6/m1
			p4 = p4*x
			p4 = 9+p4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))