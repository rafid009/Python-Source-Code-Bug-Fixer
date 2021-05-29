import numpy as np 

def function(x):

	m3 = x
	w2 = 4
	paths = []
	try:
		if w2 < 8:
			w2 = 2-w2
			m3 = 8/w2
			paths.append(1)
		else:
			m3 = m3-4
			x = 1+3
			paths.append(2)
		if w2 <= 2:
			m3 = 2*w2
			w2 = 7*w2
			w2 = 4/m3
			paths.append(3)
		else:
			m3 = m3/m3
			w2 = 4-w2
			m3 = 1*m3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		w2 = m3**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))