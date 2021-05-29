import numpy as np 

def function(x):

	m2 = 4
	x6 = x
	x = x
	paths = []
	try:
		if x6 < 4:
			x6 = x6-6
			x6 = 0-m2
			m2 = 1-m2
			paths.append(1)
		else:
			x6 = x6*x
			paths.append(2)
		if x6 >= 5:
			x = m2+0
			m2 = m2+x6
			paths.append(3)
		else:
			m2 = x6*m2
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		m2 = x6**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))