import numpy as np 

def function(x):

	v9 = 5
	m2 = x
	paths = []
	try:
		if m2 <= 7:
			m2 = v9/m2
			x = 6*x
			m2 = v9+2
			paths.append(1)
		else:
			x = m2+x
			v9 = v9*v9
			x = x-6
			paths.append(2)
		if v9 >= 1:
			x = 4+x
			m2 = 6+8
			paths.append(3)
		else:
			x = x+7
			v9 = v9-9
			m2 = 7+5
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