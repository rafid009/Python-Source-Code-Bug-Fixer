import numpy as np 

def function(x):

	d2 = x
	m9 = 1
	paths = []
	try:
		if m9 >= 4:
			m9 = m9-6
			x = x*9
			d2 = d2+d2
			paths.append(1)
		else:
			m9 = 5-4
			paths.append(2)
		if x <= 1:
			x = x/6
			m9 = m9*m9
			d2 = 5*2
			paths.append(3)
		else:
			x = 1-x
			x = d2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))