import numpy as np 

def function(x):

	m6 = 9
	t0 = 9
	paths = []
	try:
		if x <= 5:
			x = 1/x
			paths.append(1)
		else:
			m6 = t0*m6
			paths.append(2)
		if t0 > 5:
			m6 = 6*m6
			t0 = 9+t0
			t0 = t0-x
			paths.append(3)
		else:
			x = x/m6
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))