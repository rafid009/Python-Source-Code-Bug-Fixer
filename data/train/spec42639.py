import numpy as np 

def function(x):

	m3 = 1
	p2 = 4
	paths = []
	try:
		if x >= 7:
			m3 = m3-6
			x = 3/7
			x = p2/x
			paths.append(1)
		else:
			p2 = 4*m3
			paths.append(2)
		if m3 > 9:
			x = 8-x
			paths.append(3)
		else:
			p2 = 0-p2
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))