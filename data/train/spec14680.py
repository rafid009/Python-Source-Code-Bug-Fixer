import numpy as np 

def function(x):

	m4 = x
	d5 = 4
	x = x
	paths = []
	try:
		if m4 <= 4:
			x = 2-d5
			d5 = 7+5
			paths.append(1)
		else:
			m4 = m4-4
			paths.append(2)
		if d5 <= 3:
			d5 = 9/d5
			x = x*x
			d5 = m4*5
			paths.append(3)
		else:
			x = x/4
			d5 = m4-x
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