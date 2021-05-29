import numpy as np 

def function(x):

	t6 = 2
	m2 = x
	paths = []
	try:
		if t6 > 6:
			x = x*m2
			x = x-x
			paths.append(1)
		else:
			t6 = t6/m2
			t6 = x*8
			t6 = 4*9
			paths.append(2)
		if t6 <= 0:
			t6 = t6/2
			paths.append(3)
		else:
			t6 = m2+m2
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))