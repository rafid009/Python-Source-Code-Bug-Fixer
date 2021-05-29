import numpy as np 

def function(x):

	m1 = 1
	t4 = 9
	paths = []
	try:
		if m1 >= 7:
			m1 = m1*t4
			paths.append(1)
		else:
			t4 = t4/4
			paths.append(2)
		if x > 7:
			m1 = m1*6
			x = 7+x
			t4 = 4-x
			paths.append(3)
		else:
			m1 = x/m1
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