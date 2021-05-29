import numpy as np 

def function(x):

	w2 = 2
	m2 = x
	x = 9
	paths = []
	try:
		if m2 < 4:
			w2 = 2+w2
			paths.append(1)
		else:
			x = 4/x
			m2 = 1/2
			m2 = 8+2
			paths.append(2)
		if x > 3:
			x = 3*x
			m2 = m2-0
			x = 0-x
			paths.append(3)
		else:
			m2 = m2/x
			w2 = w2+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))