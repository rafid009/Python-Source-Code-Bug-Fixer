import numpy as np 

def function(x):

	w6 = 8
	m5 = 2
	paths = []
	try:
		if w6 >= 4:
			w6 = w6/2
			x = x+9
			paths.append(1)
		else:
			m5 = 3*m5
			x = 4+x
			paths.append(2)
		if x > 6:
			x = x-8
			m5 = 7-x
			paths.append(3)
		else:
			m5 = 6+m5
			x = 9+x
			m5 = 7+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))