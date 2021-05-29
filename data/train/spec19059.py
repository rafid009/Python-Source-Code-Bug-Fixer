import numpy as np 

def function(x):

	r0 = 9
	m1 = x
	paths = []
	try:
		if m1 >= 0:
			x = 2/x
			r0 = r0/6
			paths.append(1)
		else:
			r0 = r0*3
			paths.append(2)
		if r0 <= 9:
			x = r0/2
			paths.append(3)
		else:
			x = 5-x
			x = 9+9
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))