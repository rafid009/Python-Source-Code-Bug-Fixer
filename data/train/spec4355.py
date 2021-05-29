import numpy as np 

def function(x):

	m8 = x
	w2 = 1
	x = 4
	paths = []
	try:
		if w2 < 5:
			x = 0-6
			w2 = m8/m8
			paths.append(1)
		else:
			w2 = w2-5
			x = 6*9
			paths.append(2)
		if w2 >= 9:
			x = x*w2
			w2 = w2*7
			m8 = 6*w2
			paths.append(3)
		else:
			m8 = x-4
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		w2 = m8**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))