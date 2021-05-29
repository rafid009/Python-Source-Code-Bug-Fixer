import numpy as np 

def function(x):

	m2 = x
	d1 = 8
	paths = []
	try:
		if x > 3:
			d1 = 3/d1
			m2 = m2/x
			d1 = d1+x
			paths.append(1)
		else:
			m2 = m2+m2
			paths.append(2)
		if d1 <= 5:
			m2 = 0*m2
			paths.append(3)
		else:
			x = x+0
			x = 3*4
			x = m2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))