import numpy as np 

def function(x):

	m8 = 7
	w5 = x
	paths = []
	try:
		if x <= 2:
			x = x-8
			m8 = x-1
			paths.append(1)
		else:
			m8 = m8+3
			x = 7+x
			paths.append(2)
		if w5 >= 7:
			m8 = 9-m8
			x = x+x
			paths.append(3)
		else:
			m8 = m8/m8
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))