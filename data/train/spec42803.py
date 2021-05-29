import numpy as np 

def function(x):

	m6 = x
	v1 = x
	paths = []
	try:
		if x >= 2:
			m6 = 1/4
			x = x-6
			v1 = x+4
			paths.append(1)
		else:
			m6 = 4*m6
			v1 = v1-8
			v1 = 7/4
			paths.append(2)
		if m6 >= 1:
			x = x+0
			v1 = x*v1
			x = 8/v1
			paths.append(3)
		else:
			x = 4+x
			x = x/v1
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))