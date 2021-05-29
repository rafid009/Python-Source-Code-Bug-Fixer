import numpy as np 

def function(x):

	m6 = 7
	r8 = 5
	paths = []
	try:
		if r8 <= 0:
			x = 4+3
			x = 7-x
			m6 = 1-m6
			paths.append(1)
		else:
			r8 = 5+r8
			r8 = x*r8
			paths.append(2)
		if m6 >= 3:
			r8 = 3/x
			m6 = m6+8
			paths.append(3)
		else:
			r8 = r8+r8
			r8 = 4+m6
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))