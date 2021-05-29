import numpy as np 

def function(x):

	m9 = 8
	k5 = 7
	x = x
	paths = []
	try:
		if k5 > 0:
			m9 = m9+5
			m9 = m9+0
			k5 = 7*5
			paths.append(1)
		else:
			k5 = 1-3
			k5 = 4-3
			paths.append(2)
		if m9 < 1:
			k5 = k5+8
			m9 = m9-4
			x = 7+3
			paths.append(3)
		else:
			k5 = m9*2
			k5 = 9-k5
			x = x-6
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))