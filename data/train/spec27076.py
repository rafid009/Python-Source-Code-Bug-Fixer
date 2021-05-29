import numpy as np 

def function(x):

	m1 = 5
	k7 = 0
	paths = []
	try:
		if k7 > 6:
			k7 = x*k7
			m1 = 5-m1
			m1 = 6-5
			paths.append(1)
		else:
			k7 = k7-2
			paths.append(2)
		if x > 2:
			k7 = k7+5
			k7 = k7-9
			paths.append(3)
		else:
			x = x+x
			k7 = 4*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))