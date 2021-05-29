import numpy as np 

def function(x):

	r4 = 8
	r8 = x
	paths = []
	try:
		if x > 7:
			r8 = r8*7
			paths.append(1)
		else:
			r4 = r4-7
			paths.append(2)
		if r8 > 0:
			x = x/5
			x = x*6
			paths.append(3)
		else:
			x = x-5
			x = 6-6
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))