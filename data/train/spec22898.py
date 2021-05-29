import numpy as np 

def function(x):

	m7 = x
	w0 = x
	paths = []
	try:
		if w0 >= 5:
			w0 = m7*w0
			x = x+x
			x = 8-0
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if x > 9:
			x = x-w0
			m7 = 8/m7
			x = x+5
			paths.append(3)
		else:
			w0 = w0-7
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		x = w0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))