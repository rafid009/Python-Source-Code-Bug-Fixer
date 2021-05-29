import numpy as np 

def function(x):

	b1 = 1
	m3 = x
	paths = []
	try:
		if b1 < 8:
			b1 = b1/6
			b1 = b1+b1
			paths.append(1)
		else:
			x = 0*x
			m3 = 7-0
			paths.append(2)
		if b1 > 5:
			x = 1*b1
			m3 = m3-m3
			m3 = 2/x
			paths.append(3)
		else:
			b1 = b1*2
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))