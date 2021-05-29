import numpy as np 

def function(x):

	m4 = 4
	w6 = 9
	paths = []
	try:
		if w6 >= 6:
			m4 = x-w6
			m4 = 1-m4
			paths.append(1)
		else:
			x = x/w6
			m4 = m4*3
			m4 = w6+m4
			paths.append(2)
		if w6 > 8:
			w6 = 9/w6
			w6 = 0-4
			paths.append(3)
		else:
			w6 = w6-7
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		w6 = m4**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))