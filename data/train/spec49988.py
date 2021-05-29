import numpy as np 

def function(x):

	i1 = 5
	m2 = 2
	paths = []
	try:
		if i1 <= 4:
			m2 = 2-m2
			i1 = i1/6
			paths.append(1)
		else:
			i1 = i1*m2
			i1 = i1-x
			m2 = 9+x
			paths.append(2)
		if m2 < 6:
			m2 = m2/x
			x = 6*x
			x = x-5
			paths.append(3)
		else:
			m2 = m2+7
			x = m2-x
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