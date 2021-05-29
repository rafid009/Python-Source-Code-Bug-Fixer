import numpy as np 

def function(x):

	i7 = 7
	r3 = 7
	paths = []
	try:
		if r3 <= 2:
			r3 = x/r3
			paths.append(1)
		else:
			i7 = 6*4
			i7 = x*i7
			paths.append(2)
		if x <= 5:
			x = 8*5
			i7 = 9/i7
			paths.append(3)
		else:
			x = 6/x
			x = x-5
			r3 = 6-r3
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))