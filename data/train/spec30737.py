import numpy as np 

def function(x):

	m0 = 8
	n5 = x
	paths = []
	try:
		if x > 8:
			n5 = x/6
			n5 = 9-3
			n5 = 4*9
			paths.append(1)
		else:
			x = n5/9
			n5 = n5+5
			paths.append(2)
		if m0 >= 1:
			m0 = 5-n5
			x = 3*x
			x = n5*0
			paths.append(3)
		else:
			x = 9*x
			x = 5+x
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