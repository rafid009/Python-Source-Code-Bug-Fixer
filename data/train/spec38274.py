import numpy as np 

def function(x):

	x6 = 6
	r7 = x
	paths = []
	try:
		if x6 >= 2:
			x6 = x6+x
			x = 8*4
			paths.append(1)
		else:
			x6 = 7-x
			x = x+0
			paths.append(2)
		if x6 < 7:
			x = r7/x
			x = x+0
			r7 = r7-6
			paths.append(3)
		else:
			x6 = 7*2
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))