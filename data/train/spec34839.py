import numpy as np 

def function(x):

	j7 = 0
	m1 = x
	paths = []
	try:
		if j7 > 4:
			m1 = m1-3
			paths.append(1)
		else:
			m1 = 4-m1
			x = 3*x
			j7 = x+j7
			paths.append(2)
		if x <= 7:
			x = x-8
			paths.append(3)
		else:
			j7 = 6+j7
			j7 = x*j7
			x = 8-x
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