import numpy as np 

def function(x):

	r4 = 3
	i5 = x
	paths = []
	try:
		if r4 <= 6:
			r4 = r4*7
			r4 = i5/r4
			paths.append(1)
		else:
			r4 = i5*2
			paths.append(2)
		if r4 > 9:
			i5 = i5/x
			x = 4*x
			paths.append(3)
		else:
			i5 = 2/i5
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		i5 = r4**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))