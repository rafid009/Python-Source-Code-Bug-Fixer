import numpy as np 

def function(x):

	w9 = x
	m0 = 3
	paths = []
	try:
		if x > 0:
			m0 = 5*m0
			paths.append(1)
		else:
			x = x/5
			w9 = w9/3
			m0 = m0*6
			paths.append(2)
		if m0 >= 5:
			m0 = x/m0
			m0 = 4+x
			paths.append(3)
		else:
			x = w9-2
			w9 = w9/5
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))