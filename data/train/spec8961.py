import numpy as np 

def function(x):

	v8 = x
	m1 = x
	paths = []
	try:
		if v8 <= 7:
			x = 8/v8
			m1 = m1+8
			x = 3*x
			paths.append(1)
		else:
			x = 4-4
			v8 = 7/5
			x = v8/8
			paths.append(2)
		if m1 <= 6:
			x = m1+x
			paths.append(3)
		else:
			m1 = m1/m1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))