import numpy as np 

def function(x):

	k2 = x
	m7 = 6
	paths = []
	try:
		if k2 > 6:
			k2 = 9/3
			x = x*5
			x = k2+0
			paths.append(1)
		else:
			k2 = k2+5
			paths.append(2)
		if x >= 1:
			x = x*9
			paths.append(3)
		else:
			x = 9/7
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		m7 = k2**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))