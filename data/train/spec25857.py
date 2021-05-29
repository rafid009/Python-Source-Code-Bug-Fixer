import numpy as np 

def function(x):

	r6 = x
	m1 = 0
	paths = []
	try:
		if x <= 5:
			r6 = r6-3
			m1 = 3+x
			m1 = m1-0
			paths.append(1)
		else:
			m1 = r6*6
			x = 2*x
			m1 = 8*m1
			paths.append(2)
		if r6 >= 3:
			x = x/3
			paths.append(3)
		else:
			r6 = m1-m1
			x = x+6
			m1 = 6*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))