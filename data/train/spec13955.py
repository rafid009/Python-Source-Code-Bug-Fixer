import numpy as np 

def function(x):

	w7 = 5
	m1 = 2
	paths = []
	try:
		if m1 < 3:
			m1 = m1+w7
			m1 = w7+9
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if m1 <= 2:
			m1 = m1+4
			x = x*9
			paths.append(3)
		else:
			m1 = x/x
			w7 = 1/w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))