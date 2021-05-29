import numpy as np 

def function(x):

	t4 = x
	m0 = x
	paths = []
	try:
		if m0 >= 7:
			x = t4*x
			x = x/m0
			x = 3+5
			paths.append(1)
		else:
			m0 = m0+8
			paths.append(2)
		if t4 < 9:
			x = 6+x
			paths.append(3)
		else:
			t4 = t4+x
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