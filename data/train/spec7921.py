import numpy as np 

def function(x):

	m2 = 4
	r1 = x
	paths = []
	try:
		if x <= 3:
			r1 = r1/9
			r1 = 6-7
			paths.append(1)
		else:
			r1 = 1+6
			m2 = x*m2
			r1 = r1+5
			paths.append(2)
		if r1 > 6:
			r1 = 6/r1
			paths.append(3)
		else:
			m2 = 7+2
			r1 = r1-4
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))