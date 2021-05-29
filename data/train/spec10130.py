import numpy as np 

def function(x):

	a3 = x
	m2 = 2
	paths = []
	try:
		if m2 <= 9:
			a3 = 1/a3
			a3 = a3+1
			paths.append(1)
		else:
			x = x*m2
			paths.append(2)
		if x < 1:
			m2 = m2*7
			a3 = 2*a3
			m2 = m2+m2
			paths.append(3)
		else:
			x = m2*3
			a3 = 5/a3
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