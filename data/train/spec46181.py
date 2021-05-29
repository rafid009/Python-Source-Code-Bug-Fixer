import numpy as np 

def function(x):

	v5 = 2
	m8 = 2
	x = x
	paths = []
	try:
		if v5 <= 6:
			v5 = 5+v5
			v5 = x/v5
			paths.append(1)
		else:
			x = x*m8
			paths.append(2)
		if v5 <= 2:
			v5 = v5-0
			m8 = m8*m8
			v5 = v5+v5
			paths.append(3)
		else:
			x = x*m8
			m8 = v5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))