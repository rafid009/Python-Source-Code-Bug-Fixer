import numpy as np 

def function(x):

	w9 = x
	m0 = x
	x = 9
	paths = []
	try:
		if x < 7:
			x = 8+7
			x = x-w9
			x = x/x
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if w9 > 0:
			w9 = w9*5
			m0 = m0/4
			x = m0/6
			paths.append(3)
		else:
			x = 0*2
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		w9 = w9**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))