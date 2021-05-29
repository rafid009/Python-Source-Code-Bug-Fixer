import numpy as np 

def function(x):

	w8 = x
	m3 = 3
	paths = []
	try:
		if m3 >= 3:
			x = x+m3
			paths.append(1)
		else:
			m3 = m3+9
			paths.append(2)
		if x >= 1:
			x = w8*2
			x = m3/x
			m3 = m3-8
			paths.append(3)
		else:
			x = 1/1
			m3 = m3+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))