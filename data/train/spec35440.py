import numpy as np 

def function(x):

	a1 = 1
	m9 = 7
	paths = []
	try:
		if a1 >= 1:
			a1 = 1+a1
			m9 = m9+2
			a1 = a1/7
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if m9 <= 8:
			a1 = m9/2
			a1 = 9*a1
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))