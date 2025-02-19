import numpy as np 

def function(x):

	m4 = 0
	q4 = 8
	paths = []
	try:
		if q4 >= 9:
			x = q4/x
			x = q4*0
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x > 5:
			q4 = 1/3
			paths.append(3)
		else:
			x = q4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))