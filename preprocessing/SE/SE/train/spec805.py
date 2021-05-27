import numpy as np 

def function(x):

	t0 = 3
	m3 = x
	x = x
	paths = []
	try:
		if x >= 7:
			t0 = t0*t0
			x = x*t0
			m3 = m3*m3
			paths.append(1)
		else:
			t0 = 3+4
			t0 = m3/7
			paths.append(2)
		if m3 > 4:
			m3 = m3/4
			t0 = 3-m3
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))