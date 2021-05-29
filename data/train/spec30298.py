import numpy as np 

def function(x):

	m0 = x
	r2 = 7
	x = 3
	paths = []
	try:
		if r2 <= 6:
			r2 = r2+1
			r2 = r2/9
			x = x-6
			paths.append(1)
		else:
			r2 = 9/6
			x = 6/4
			x = 7-x
			paths.append(2)
		if m0 <= 0:
			r2 = r2*2
			r2 = r2/1
			paths.append(3)
		else:
			m0 = 9*m0
			x = x/6
			m0 = m0-x
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))