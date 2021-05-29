import numpy as np 

def function(x):

	r9 = x
	i7 = x
	paths = []
	try:
		if r9 < 5:
			i7 = i7/x
			r9 = 3-r9
			i7 = i7-8
			paths.append(1)
		else:
			i7 = r9*2
			i7 = 6+i7
			paths.append(2)
		if r9 <= 5:
			x = x*7
			r9 = i7*9
			paths.append(3)
		else:
			x = 0+5
			r9 = i7*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))