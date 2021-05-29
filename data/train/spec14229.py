import numpy as np 

def function(x):

	r7 = x
	m8 = x
	paths = []
	try:
		if x < 6:
			r7 = 3-x
			x = x-3
			m8 = m8/2
			paths.append(1)
		else:
			x = x-x
			x = 1-x
			x = m8*x
			paths.append(2)
		if r7 >= 0:
			x = 2*x
			r7 = 1-r7
			m8 = m8+x
			paths.append(3)
		else:
			x = 4+9
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		r7 = m8**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))