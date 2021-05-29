import numpy as np 

def function(x):

	w6 = x
	m1 = 0
	paths = []
	try:
		if x > 6:
			m1 = 2-m1
			w6 = w6-0
			paths.append(1)
		else:
			w6 = 3+w6
			paths.append(2)
		if m1 <= 2:
			w6 = x/8
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))