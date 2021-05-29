import numpy as np 

def function(x):

	v9 = x
	m2 = x
	x = x
	paths = []
	try:
		if v9 < 0:
			v9 = 1*v9
			paths.append(1)
		else:
			x = x/m2
			m2 = 8+m2
			v9 = v9+v9
			paths.append(2)
		if x <= 2:
			v9 = v9/x
			v9 = 6/v9
			v9 = x+v9
			paths.append(3)
		else:
			x = 5*x
			m2 = 5-0
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		v9 = m2**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))