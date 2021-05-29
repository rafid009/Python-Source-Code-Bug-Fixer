import numpy as np 

def function(x):

	i7 = 8
	r5 = x
	paths = []
	try:
		if x <= 4:
			i7 = 1/2
			paths.append(1)
		else:
			x = i7/x
			i7 = i7-7
			i7 = x/i7
			paths.append(2)
		if i7 <= 2:
			r5 = r5+r5
			paths.append(3)
		else:
			x = x/9
			r5 = 3/x
			x = 1-2
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))