import numpy as np 

def function(x):

	w1 = x
	m4 = x
	paths = []
	try:
		if w1 >= 3:
			m4 = 6+m4
			paths.append(1)
		else:
			m4 = 6/m4
			paths.append(2)
		if w1 <= 1:
			x = x/6
			paths.append(3)
		else:
			x = x*9
			w1 = m4/w1
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