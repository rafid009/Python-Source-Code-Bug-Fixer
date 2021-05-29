import numpy as np 

def function(x):

	r8 = 9
	m1 = x
	paths = []
	try:
		if r8 > 6:
			r8 = 5-r8
			paths.append(1)
		else:
			x = r8*x
			r8 = 1-x
			paths.append(2)
		if m1 > 3:
			x = x*1
			paths.append(3)
		else:
			m1 = 4*x
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))