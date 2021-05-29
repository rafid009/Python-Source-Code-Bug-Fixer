import numpy as np 

def function(x):

	m4 = 4
	d2 = x
	paths = []
	try:
		if d2 > 7:
			x = x+0
			x = 5-x
			m4 = 5+m4
			paths.append(1)
		else:
			m4 = 3*m4
			d2 = 1*0
			x = x*4
			paths.append(2)
		if d2 >= 5:
			m4 = m4/1
			paths.append(3)
		else:
			x = d2-x
			m4 = 0-m4
			x = x*m4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))