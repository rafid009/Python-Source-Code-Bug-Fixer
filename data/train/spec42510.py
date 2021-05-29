import numpy as np 

def function(x):

	b6 = 0
	m4 = x
	paths = []
	try:
		if b6 < 2:
			x = x*1
			b6 = 2*b6
			paths.append(1)
		else:
			b6 = b6+6
			x = m4-m4
			paths.append(2)
		if b6 <= 0:
			x = x-7
			b6 = b6*4
			paths.append(3)
		else:
			x = x/8
			b6 = 0+b6
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))