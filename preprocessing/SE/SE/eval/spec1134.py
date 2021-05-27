import numpy as np 

def function(x):

	m7 = x
	d4 = 8
	paths = []
	try:
		if m7 >= 0:
			d4 = 2/d4
			x = d4+d4
			d4 = 8/7
			paths.append(1)
		else:
			d4 = 5+0
			m7 = m7/5
			paths.append(2)
		if d4 < 0:
			m7 = m7-3
			m7 = m7+x
			paths.append(3)
		else:
			d4 = d4-7
			m7 = 6-d4
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))