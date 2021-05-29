import numpy as np 

def function(x):

	w2 = x
	m9 = x
	paths = []
	try:
		if m9 < 8:
			m9 = m9-1
			x = 1/x
			paths.append(1)
		else:
			w2 = 9+w2
			paths.append(2)
		if w2 >= 0:
			x = x/2
			paths.append(3)
		else:
			w2 = m9-m9
			m9 = 2+m9
			x = x*4
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		w2 = m9**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))