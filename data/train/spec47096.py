import numpy as np 

def function(x):

	p4 = 0
	m9 = x
	paths = []
	try:
		if x <= 1:
			x = x/4
			paths.append(1)
		else:
			p4 = p4*8
			paths.append(2)
		if m9 > 1:
			m9 = m9+8
			paths.append(3)
		else:
			x = x-4
			x = 7-3
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))