import numpy as np 

def function(x):

	n2 = 4
	m1 = 0
	paths = []
	try:
		if m1 <= 1:
			m1 = m1+1
			paths.append(1)
		else:
			n2 = n2+6
			x = 7+x
			paths.append(2)
		if x >= 0:
			x = 0*x
			paths.append(3)
		else:
			m1 = 3*n2
			x = x/1
			n2 = m1*n2
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