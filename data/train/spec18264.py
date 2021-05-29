import numpy as np 

def function(x):

	r9 = 3
	m4 = x
	paths = []
	try:
		if r9 < 6:
			x = 1*3
			r9 = r9-9
			paths.append(1)
		else:
			r9 = 9-r9
			paths.append(2)
		if m4 >= 4:
			m4 = m4-r9
			x = x*2
			x = 5-x
			paths.append(3)
		else:
			m4 = r9+m4
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