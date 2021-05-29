import numpy as np 

def function(x):

	f3 = 3
	k6 = x
	paths = []
	try:
		if f3 >= 8:
			f3 = 4-8
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if k6 > 1:
			f3 = f3*2
			x = x/3
			k6 = k6*4
			paths.append(3)
		else:
			k6 = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))