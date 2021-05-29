import numpy as np 

def function(x):

	w4 = 3
	m3 = 2
	paths = []
	try:
		if m3 > 4:
			m3 = m3-w4
			w4 = 9-w4
			paths.append(1)
		else:
			x = m3*8
			x = w4-x
			m3 = 1+m3
			paths.append(2)
		if x <= 0:
			w4 = w4*x
			w4 = w4*8
			m3 = m3+m3
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))