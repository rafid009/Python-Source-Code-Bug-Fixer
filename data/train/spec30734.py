import numpy as np 

def function(x):

	m0 = 8
	t0 = x
	x = 9
	paths = []
	try:
		if t0 < 5:
			m0 = m0*0
			x = x-0
			t0 = 8+t0
			paths.append(1)
		else:
			t0 = 0-t0
			t0 = t0/5
			paths.append(2)
		if t0 > 0:
			m0 = 0-4
			x = 2*x
			x = 9*m0
			paths.append(3)
		else:
			m0 = 9+x
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))