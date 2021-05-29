import numpy as np 

def function(x):

	m6 = x
	w3 = 5
	paths = []
	try:
		if x <= 7:
			x = 2*x
			x = w3*w3
			m6 = 5/m6
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if m6 < 1:
			x = x*x
			m6 = m6*5
			w3 = w3-m6
			paths.append(3)
		else:
			m6 = 9/7
			w3 = w3+w3
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))