import numpy as np 

def function(x):

	f6 = x
	r5 = x
	paths = []
	try:
		if x < 7:
			r5 = r5-3
			paths.append(1)
		else:
			f6 = f6+5
			paths.append(2)
		if r5 >= 3:
			x = 9+x
			f6 = f6/6
			f6 = 8+5
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))