import numpy as np 

def function(x):

	e6 = x
	m2 = x
	paths = []
	try:
		if m2 <= 4:
			x = x+6
			paths.append(1)
		else:
			m2 = 6/m2
			paths.append(2)
		if x >= 7:
			m2 = 5+x
			paths.append(3)
		else:
			e6 = e6/2
			m2 = m2/2
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))