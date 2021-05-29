import numpy as np 

def function(x):

	m2 = 1
	k6 = 4
	x = x
	paths = []
	try:
		if x <= 5:
			m2 = 2+8
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if k6 < 3:
			x = x+k6
			m2 = m2-2
			paths.append(3)
		else:
			m2 = 5-3
			m2 = x+m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		k6 = m2**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))