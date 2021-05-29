import numpy as np 

def function(x):

	m4 = 8
	r5 = x
	paths = []
	try:
		if x <= 1:
			m4 = m4/r5
			paths.append(1)
		else:
			r5 = 1/7
			r5 = r5*3
			paths.append(2)
		if m4 > 7:
			x = x/4
			r5 = 5+r5
			x = x*m4
			paths.append(3)
		else:
			r5 = r5-9
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