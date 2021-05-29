import numpy as np 

def function(x):

	m3 = 8
	b1 = 1
	paths = []
	try:
		if x < 7:
			b1 = x/b1
			m3 = 8/m3
			paths.append(1)
		else:
			b1 = 9+b1
			m3 = 8-8
			x = 1/x
			paths.append(2)
		if m3 <= 8:
			x = 9-m3
			m3 = b1*x
			paths.append(3)
		else:
			x = x*9
			b1 = b1-2
			b1 = 3+2
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		b1 = m3**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))