import numpy as np 

def function(x):

	w6 = x
	m5 = 8
	paths = []
	try:
		if w6 > 8:
			w6 = 1*w6
			w6 = 4/1
			w6 = w6-7
			paths.append(1)
		else:
			m5 = 1+m5
			m5 = 8*4
			paths.append(2)
		if x < 3:
			w6 = 5/w6
			w6 = w6/8
			paths.append(3)
		else:
			w6 = m5/8
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