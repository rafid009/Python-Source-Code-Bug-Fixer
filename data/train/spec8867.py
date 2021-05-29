import numpy as np 

def function(x):

	m1 = 4
	r5 = x
	paths = []
	try:
		if r5 >= 1:
			r5 = 8-5
			paths.append(1)
		else:
			r5 = x+r5
			m1 = m1/x
			paths.append(2)
		if m1 <= 2:
			m1 = 7/4
			paths.append(3)
		else:
			m1 = 9/2
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))