import numpy as np 

def function(x):

	h2 = 7
	m6 = 2
	paths = []
	try:
		if m6 <= 3:
			h2 = h2-2
			m6 = 5/m6
			h2 = x+1
			paths.append(1)
		else:
			m6 = m6/6
			paths.append(2)
		if h2 > 4:
			x = x+9
			h2 = m6+6
			x = x*1
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))