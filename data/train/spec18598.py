import numpy as np 

def function(x):

	d8 = x
	m9 = x
	paths = []
	try:
		if m9 <= 1:
			d8 = d8/8
			paths.append(1)
		else:
			m9 = m9*m9
			paths.append(2)
		if d8 >= 8:
			d8 = x*d8
			m9 = m9*1
			paths.append(3)
		else:
			m9 = m9*m9
			m9 = m9*2
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))