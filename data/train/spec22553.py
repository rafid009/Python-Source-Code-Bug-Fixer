import numpy as np 

def function(x):

	m3 = 6
	w1 = 1
	paths = []
	try:
		if w1 <= 3:
			w1 = w1+9
			paths.append(1)
		else:
			x = m3/x
			x = 0+6
			x = m3/x
			paths.append(2)
		if m3 > 9:
			w1 = w1-0
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))