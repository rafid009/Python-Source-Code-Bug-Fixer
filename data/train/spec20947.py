import numpy as np 

def function(x):

	m2 = x
	t4 = x
	paths = []
	try:
		if m2 < 7:
			x = x+2
			m2 = 9+x
			x = m2-x
			paths.append(1)
		else:
			t4 = t4+9
			t4 = 8+x
			m2 = 5+m2
			paths.append(2)
		if t4 < 1:
			m2 = x/6
			t4 = t4-0
			x = 2-x
			paths.append(3)
		else:
			x = 9*x
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