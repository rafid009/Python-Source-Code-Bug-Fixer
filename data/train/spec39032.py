import numpy as np 

def function(x):

	h5 = 8
	m9 = x
	x = x
	paths = []
	try:
		if x < 7:
			h5 = 4+4
			x = x*2
			m9 = x/m9
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x <= 4:
			m9 = 5/m9
			m9 = m9-7
			h5 = 4-h5
			paths.append(3)
		else:
			h5 = m9*7
			m9 = 6/8
			m9 = m9+x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))