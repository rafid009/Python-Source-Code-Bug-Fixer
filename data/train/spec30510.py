import numpy as np 

def function(x):

	m4 = x
	a0 = x
	x = x
	paths = []
	try:
		if x > 5:
			m4 = 0-9
			a0 = 8*0
			x = 7*4
			paths.append(1)
		else:
			x = x*1
			a0 = a0-a0
			a0 = a0-x
			paths.append(2)
		if a0 >= 2:
			x = 3-m4
			paths.append(3)
		else:
			x = 0-x
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