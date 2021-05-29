import numpy as np 

def function(x):

	h5 = 2
	m1 = 6
	paths = []
	try:
		if m1 >= 6:
			m1 = m1*x
			h5 = x*5
			x = x+2
			paths.append(1)
		else:
			x = 5+5
			paths.append(2)
		if m1 <= 8:
			x = h5+x
			x = 7*2
			paths.append(3)
		else:
			x = 7*1
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))