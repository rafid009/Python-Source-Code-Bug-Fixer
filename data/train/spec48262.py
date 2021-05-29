import numpy as np 

def function(x):

	m7 = x
	d0 = x
	paths = []
	try:
		if x >= 0:
			x = x*4
			x = x-d0
			paths.append(1)
		else:
			m7 = m7-7
			d0 = d0*3
			x = x/6
			paths.append(2)
		if m7 < 3:
			d0 = m7+0
			m7 = m7-0
			m7 = m7*8
			paths.append(3)
		else:
			d0 = 1*d0
			m7 = m7-7
			x = m7*5
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))