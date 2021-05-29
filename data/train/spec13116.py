import numpy as np 

def function(x):

	m2 = 2
	k1 = x
	x = 2
	paths = []
	try:
		if m2 <= 4:
			x = k1*7
			paths.append(1)
		else:
			x = x/m2
			paths.append(2)
		if m2 < 8:
			m2 = m2/2
			m2 = 0/m2
			paths.append(3)
		else:
			k1 = 1*m2
			x = 4/4
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))