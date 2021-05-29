import numpy as np 

def function(x):

	o0 = 9
	p9 = x
	paths = []
	try:
		if p9 >= 2:
			x = x*p9
			x = x*9
			paths.append(1)
		else:
			o0 = p9/x
			x = 1-8
			x = o0/3
			paths.append(2)
		if p9 > 4:
			x = 1/1
			o0 = 3/o0
			paths.append(3)
		else:
			o0 = 7/3
			o0 = o0-5
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		x = o0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))