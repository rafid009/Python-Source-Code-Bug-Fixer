import numpy as np 

def function(x):

	m9 = x
	w2 = x
	paths = []
	try:
		if m9 <= 2:
			x = 1+x
			w2 = w2*1
			paths.append(1)
		else:
			x = 3-0
			paths.append(2)
		if x < 9:
			w2 = w2-m9
			w2 = 4/9
			x = m9/x
			paths.append(3)
		else:
			m9 = 2+4
			w2 = w2/9
			w2 = w2/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))