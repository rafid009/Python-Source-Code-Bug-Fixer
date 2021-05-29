import numpy as np 

def function(x):

	m9 = x
	w5 = 8
	paths = []
	try:
		if m9 < 6:
			w5 = x*w5
			w5 = 7/w5
			w5 = w5*8
			paths.append(1)
		else:
			w5 = 9-x
			paths.append(2)
		if x >= 8:
			w5 = w5/w5
			paths.append(3)
		else:
			w5 = w5+5
			w5 = 0+0
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m9 = m9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))