import numpy as np 

def function(x):

	m6 = 6
	k2 = 6
	paths = []
	try:
		if x < 4:
			x = x*x
			k2 = 3/k2
			x = x-k2
			paths.append(1)
		else:
			m6 = 3*k2
			x = 0*5
			paths.append(2)
		if m6 <= 6:
			k2 = x*k2
			paths.append(3)
		else:
			k2 = x+0
			x = 7+3
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		m6 = k2**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))