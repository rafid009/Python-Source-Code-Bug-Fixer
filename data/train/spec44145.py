import numpy as np 

def function(x):

	v3 = 0
	m9 = 8
	paths = []
	try:
		if v3 >= 6:
			v3 = 4+v3
			paths.append(1)
		else:
			m9 = 3+x
			m9 = v3-m9
			x = x*4
			paths.append(2)
		if x < 8:
			m9 = 6*m9
			m9 = m9/5
			v3 = v3-x
			paths.append(3)
		else:
			v3 = v3*x
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