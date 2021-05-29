import numpy as np 

def function(x):

	r3 = 6
	m0 = x
	paths = []
	try:
		if m0 > 3:
			m0 = 7+m0
			x = r3+x
			r3 = 4-r3
			paths.append(1)
		else:
			r3 = r3+m0
			paths.append(2)
		if m0 > 3:
			m0 = 4/1
			x = x-2
			paths.append(3)
		else:
			x = x*3
			r3 = m0/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))