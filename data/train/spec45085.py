import numpy as np 

def function(x):

	d3 = 7
	m7 = x
	paths = []
	try:
		if x <= 3:
			x = 5-7
			x = 1*d3
			m7 = d3*m7
			paths.append(1)
		else:
			x = d3*x
			x = x*5
			d3 = 4-0
			paths.append(2)
		if m7 >= 4:
			m7 = x+2
			d3 = x*6
			paths.append(3)
		else:
			d3 = 6/d3
			d3 = 3*d3
			m7 = m7+m7
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		m7 = m7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))