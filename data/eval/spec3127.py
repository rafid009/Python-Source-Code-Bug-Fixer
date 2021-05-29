import numpy as np 

def function(x):

	r1 = 7
	m9 = x
	paths = []
	try:
		if x >= 9:
			m9 = 9-m9
			paths.append(1)
		else:
			m9 = 1-m9
			paths.append(2)
		if m9 <= 0:
			r1 = r1/4
			x = m9+7
			paths.append(3)
		else:
			x = x+x
			r1 = x/r1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))