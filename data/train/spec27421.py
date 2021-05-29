import numpy as np 

def function(x):

	k4 = x
	m2 = x
	paths = []
	try:
		if k4 <= 8:
			x = 3+4
			paths.append(1)
		else:
			k4 = m2-k4
			x = 5-x
			k4 = x-5
			paths.append(2)
		if m2 < 6:
			x = m2+x
			m2 = m2+8
			k4 = 9-9
			paths.append(3)
		else:
			x = 3-x
			k4 = x-k4
			x = x+m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		k4 = m2**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))