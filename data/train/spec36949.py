import numpy as np 

def function(x):

	a8 = 8
	m5 = x
	paths = []
	try:
		if a8 >= 0:
			m5 = m5-5
			paths.append(1)
		else:
			m5 = a8/2
			x = x*8
			x = m5*9
			paths.append(2)
		if x > 0:
			a8 = a8+a8
			x = 3/6
			m5 = m5/x
			paths.append(3)
		else:
			m5 = 3+9
			x = x*7
			m5 = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))