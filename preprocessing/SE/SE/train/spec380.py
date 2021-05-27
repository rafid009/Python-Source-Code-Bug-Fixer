import numpy as np 

def function(x):

	m1 = 6
	r5 = 6
	paths = []
	try:
		if x <= 1:
			x = 4*5
			r5 = 1*r5
			m1 = m1/m1
			paths.append(1)
		else:
			m1 = m1-7
			paths.append(2)
		if m1 < 5:
			x = 7*x
			r5 = r5/5
			paths.append(3)
		else:
			x = m1*x
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		r5 = m1**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))