import numpy as np 

def function(x):

	j4 = x
	m6 = x
	paths = []
	try:
		if j4 >= 5:
			j4 = x*m6
			paths.append(1)
		else:
			j4 = x-j4
			m6 = m6-9
			x = x-9
			paths.append(2)
		if x < 2:
			m6 = m6-5
			j4 = j4*j4
			j4 = 9-8
			paths.append(3)
		else:
			j4 = 2+x
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