import numpy as np 

def function(x):

	d5 = x
	m4 = 5
	paths = []
	try:
		if d5 <= 4:
			x = x*6
			d5 = m4+m4
			paths.append(1)
		else:
			d5 = 7-d5
			paths.append(2)
		if m4 >= 4:
			m4 = m4-8
			d5 = x-8
			paths.append(3)
		else:
			d5 = d5+6
			d5 = m4+d5
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))