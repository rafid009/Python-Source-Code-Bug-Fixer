import numpy as np 

def function(x):

	m9 = 9
	v4 = 1
	paths = []
	try:
		if m9 <= 6:
			m9 = 5/6
			v4 = v4+5
			paths.append(1)
		else:
			v4 = x*v4
			paths.append(2)
		if x <= 6:
			m9 = m9/2
			v4 = v4/m9
			x = x+9
			paths.append(3)
		else:
			x = 1-3
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