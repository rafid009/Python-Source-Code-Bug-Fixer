import numpy as np 

def function(x):

	v5 = 9
	m8 = x
	paths = []
	try:
		if x > 5:
			x = 5-x
			paths.append(1)
		else:
			m8 = 3+m8
			paths.append(2)
		if m8 < 6:
			x = x/2
			v5 = 5/1
			x = x*1
			paths.append(3)
		else:
			v5 = 9*9
			v5 = 6/v5
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))