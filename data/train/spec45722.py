import numpy as np 

def function(x):

	b9 = 8
	m8 = x
	paths = []
	try:
		if x > 1:
			x = 3+3
			x = b9*7
			x = 0+9
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if b9 >= 2:
			m8 = b9*m8
			b9 = 3*b9
			b9 = b9*m8
			paths.append(3)
		else:
			m8 = b9*2
			b9 = 0*b9
			b9 = b9/6
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))