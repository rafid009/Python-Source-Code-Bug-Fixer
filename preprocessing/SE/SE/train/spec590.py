import numpy as np 

def function(x):

	n1 = x
	m6 = x
	paths = []
	try:
		if m6 <= 9:
			m6 = 9-m6
			m6 = 5-m6
			x = m6*n1
			paths.append(1)
		else:
			n1 = x-n1
			n1 = n1+m6
			n1 = n1-m6
			paths.append(2)
		if x < 2:
			n1 = n1-m6
			m6 = m6*n1
			paths.append(3)
		else:
			x = x+2
			n1 = n1*n1
			m6 = x/m6
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))