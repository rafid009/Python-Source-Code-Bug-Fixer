import numpy as np 

def function(x):

	m1 = x
	b2 = 8
	paths = []
	try:
		if x < 8:
			x = 8-x
			b2 = m1-5
			paths.append(1)
		else:
			b2 = x+b2
			x = x-2
			paths.append(2)
		if m1 > 7:
			b2 = 1+b2
			x = x*4
			paths.append(3)
		else:
			m1 = m1/b2
			b2 = b2*9
			x = b2/x
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