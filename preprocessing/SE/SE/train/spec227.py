import numpy as np 

def function(x):

	w2 = 8
	m9 = 8
	paths = []
	try:
		if m9 >= 8:
			w2 = w2+0
			paths.append(1)
		else:
			w2 = w2/6
			paths.append(2)
		if m9 > 2:
			w2 = w2/x
			paths.append(3)
		else:
			m9 = m9-m9
			x = 7*7
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))