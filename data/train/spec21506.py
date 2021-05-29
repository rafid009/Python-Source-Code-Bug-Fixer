import numpy as np 

def function(x):

	r2 = 4
	m8 = 9
	paths = []
	try:
		if r2 >= 7:
			m8 = m8*2
			paths.append(1)
		else:
			m8 = m8-6
			r2 = 3+0
			x = m8+x
			paths.append(2)
		if x > 1:
			r2 = m8-3
			x = 1+5
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))