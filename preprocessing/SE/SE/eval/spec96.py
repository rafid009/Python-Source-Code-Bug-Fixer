import numpy as np 

def function(x):

	m1 = x
	r0 = 9
	paths = []
	try:
		if m1 >= 4:
			x = 5*1
			x = x+3
			x = r0/x
			paths.append(1)
		else:
			x = x/x
			r0 = r0*9
			paths.append(2)
		if r0 <= 4:
			m1 = 4-m1
			r0 = 1/2
			paths.append(3)
		else:
			x = m1-r0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))