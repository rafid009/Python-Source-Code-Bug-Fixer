import numpy as np 

def function(x):

	m2 = 9
	v6 = x
	paths = []
	try:
		if m2 <= 2:
			x = x-x
			m2 = v6*m2
			paths.append(1)
		else:
			m2 = 2+9
			x = 4/x
			v6 = x/3
			paths.append(2)
		if x <= 8:
			x = x/m2
			paths.append(3)
		else:
			x = 7*x
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