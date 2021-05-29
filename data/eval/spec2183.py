import numpy as np 

def function(x):

	v6 = x
	m4 = 6
	paths = []
	try:
		if m4 > 5:
			v6 = v6+4
			m4 = 1+x
			m4 = v6/3
			paths.append(1)
		else:
			m4 = v6/x
			v6 = v6/2
			paths.append(2)
		if v6 < 0:
			v6 = v6/1
			x = 8*v6
			v6 = v6/5
			paths.append(3)
		else:
			v6 = v6+1
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