import numpy as np 

def function(x):

	b8 = x
	m1 = x
	paths = []
	try:
		if x > 8:
			x = x-x
			b8 = b8*x
			m1 = 1-m1
			paths.append(1)
		else:
			x = x+5
			b8 = 6*3
			paths.append(2)
		if m1 > 5:
			m1 = m1/2
			paths.append(3)
		else:
			b8 = b8*0
			m1 = m1-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))