import numpy as np 

def function(x):

	u2 = 8
	m2 = x
	paths = []
	try:
		if x >= 4:
			x = x+u2
			u2 = u2-9
			x = m2+x
			paths.append(1)
		else:
			m2 = 9*m2
			paths.append(2)
		if u2 < 0:
			x = x/9
			paths.append(3)
		else:
			x = m2-4
			x = x*2
			u2 = u2-u2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))