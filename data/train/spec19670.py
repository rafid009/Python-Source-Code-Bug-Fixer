import numpy as np 

def function(x):

	m8 = 4
	v6 = x
	paths = []
	try:
		if v6 > 8:
			v6 = 2/v6
			v6 = 8-v6
			paths.append(1)
		else:
			x = 0+x
			v6 = m8/v6
			paths.append(2)
		if x < 1:
			x = x/1
			v6 = v6+m8
			paths.append(3)
		else:
			v6 = m8*x
			x = x-7
			x = 8/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))