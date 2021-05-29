import numpy as np 

def function(x):

	m7 = 3
	r4 = 6
	paths = []
	try:
		if m7 <= 2:
			m7 = m7/m7
			paths.append(1)
		else:
			x = 3-x
			r4 = x*m7
			paths.append(2)
		if r4 >= 1:
			r4 = 6-m7
			x = 5-x
			m7 = x+m7
			paths.append(3)
		else:
			r4 = 0-0
			r4 = 5-r4
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		r4 = m7**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))