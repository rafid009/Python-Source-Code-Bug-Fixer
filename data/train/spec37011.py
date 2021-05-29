import numpy as np 

def function(x):

	m4 = 2
	t6 = 5
	x = x
	paths = []
	try:
		if x < 6:
			m4 = t6*m4
			m4 = 8/m4
			paths.append(1)
		else:
			m4 = 0-5
			paths.append(2)
		if m4 <= 9:
			x = 3-x
			paths.append(3)
		else:
			x = 9-4
			t6 = 9-m4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))