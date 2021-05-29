import numpy as np 

def function(x):

	w8 = x
	m5 = x
	x = 5
	paths = []
	try:
		if m5 >= 6:
			m5 = m5*m5
			paths.append(1)
		else:
			m5 = m5+1
			paths.append(2)
		if w8 >= 3:
			w8 = w8+w8
			m5 = m5/w8
			paths.append(3)
		else:
			m5 = m5+x
			x = x-w8
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))