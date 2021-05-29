import numpy as np 

def function(x):

	m4 = 6
	o0 = 0
	paths = []
	try:
		if o0 < 6:
			m4 = 2-m4
			o0 = 4+9
			o0 = 6-o0
			paths.append(1)
		else:
			m4 = 8/m4
			o0 = 5+o0
			m4 = m4+x
			paths.append(2)
		if o0 <= 1:
			x = 7+x
			m4 = 7-3
			x = o0+x
			paths.append(3)
		else:
			o0 = o0-2
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