import numpy as np 

def function(x):

	m7 = x
	w4 = x
	paths = []
	try:
		if w4 < 3:
			m7 = m7*3
			w4 = 9/w4
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if m7 < 3:
			m7 = m7-m7
			x = 3*w4
			paths.append(3)
		else:
			x = 9+5
			w4 = w4+2
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))