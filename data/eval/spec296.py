import numpy as np 

def function(x):

	w6 = x
	m7 = 8
	paths = []
	try:
		if m7 > 0:
			m7 = x+m7
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if m7 < 8:
			m7 = m7-9
			x = 7+m7
			m7 = 6-m7
			paths.append(3)
		else:
			m7 = 1+m7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))