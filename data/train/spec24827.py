import numpy as np 

def function(x):

	d3 = x
	m7 = 1
	x = 3
	paths = []
	try:
		if m7 >= 3:
			d3 = d3/9
			x = x+1
			paths.append(1)
		else:
			m7 = x*m7
			m7 = 8+m7
			m7 = 3/8
			paths.append(2)
		if m7 >= 1:
			m7 = m7*m7
			x = 7/x
			d3 = 2-d3
			paths.append(3)
		else:
			x = 0/m7
			d3 = d3+0
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		d3 = d3**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))