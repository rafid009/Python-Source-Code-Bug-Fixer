import numpy as np 

def function(x):

	d3 = 9
	m8 = x
	paths = []
	try:
		if d3 <= 4:
			d3 = 8*d3
			d3 = 4-9
			m8 = m8/d3
			paths.append(1)
		else:
			m8 = 1*m8
			m8 = 1*m8
			paths.append(2)
		if m8 >= 5:
			x = 4/x
			m8 = m8/8
			d3 = 7/d3
			paths.append(3)
		else:
			d3 = 7-d3
			d3 = 3*5
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))