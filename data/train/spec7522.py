import numpy as np 

def function(x):

	m6 = 7
	v2 = x
	paths = []
	try:
		if x <= 6:
			v2 = x/9
			paths.append(1)
		else:
			x = 7*m6
			x = 3*x
			v2 = v2/8
			paths.append(2)
		if m6 > 7:
			x = x-4
			v2 = 0/v2
			x = 6-x
			paths.append(3)
		else:
			v2 = m6+m6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))