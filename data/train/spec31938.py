import numpy as np 

def function(x):

	m4 = 4
	t0 = x
	paths = []
	try:
		if x >= 7:
			m4 = 8/m4
			x = 8*x
			paths.append(1)
		else:
			x = x*m4
			x = m4*x
			x = 4+t0
			paths.append(2)
		if x <= 4:
			m4 = 6+m4
			paths.append(3)
		else:
			m4 = t0+t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))