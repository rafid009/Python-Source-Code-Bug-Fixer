import numpy as np 

def function(x):

	m2 = x
	w8 = x
	paths = []
	try:
		if w8 <= 4:
			x = 7/x
			paths.append(1)
		else:
			x = 7*m2
			paths.append(2)
		if w8 <= 2:
			m2 = 9/m2
			x = 7+m2
			paths.append(3)
		else:
			w8 = 1/3
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))