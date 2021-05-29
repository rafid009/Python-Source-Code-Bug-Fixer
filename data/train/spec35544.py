import numpy as np 

def function(x):

	n0 = 6
	m9 = x
	paths = []
	try:
		if m9 <= 1:
			n0 = n0*8
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if n0 <= 6:
			x = x/9
			paths.append(3)
		else:
			n0 = n0+9
			m9 = m9*n0
			n0 = 6*2
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))