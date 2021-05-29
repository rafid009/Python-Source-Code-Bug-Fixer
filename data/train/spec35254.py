import numpy as np 

def function(x):

	t6 = 0
	m4 = x
	paths = []
	try:
		if t6 <= 7:
			x = 6+x
			x = x/2
			paths.append(1)
		else:
			x = m4/x
			m4 = m4/m4
			paths.append(2)
		if t6 < 1:
			t6 = 0-t6
			paths.append(3)
		else:
			x = x*x
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