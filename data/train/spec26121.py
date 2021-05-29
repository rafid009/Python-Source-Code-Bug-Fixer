import numpy as np 

def function(x):

	r5 = x
	j5 = x
	paths = []
	try:
		if r5 > 8:
			r5 = 3/r5
			r5 = r5-9
			paths.append(1)
		else:
			r5 = r5-6
			x = x+0
			j5 = 3-0
			paths.append(2)
		if x >= 9:
			x = 6-j5
			paths.append(3)
		else:
			j5 = j5-5
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