import numpy as np 

def function(x):

	b0 = 6
	m1 = x
	paths = []
	try:
		if x >= 0:
			x = 2/3
			b0 = b0-b0
			b0 = b0/7
			paths.append(1)
		else:
			b0 = b0+2
			b0 = m1/m1
			b0 = 6-b0
			paths.append(2)
		if b0 >= 7:
			m1 = m1*4
			x = x*8
			b0 = b0+b0
			paths.append(3)
		else:
			x = 8/m1
			m1 = m1*b0
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		b0 = m1**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))