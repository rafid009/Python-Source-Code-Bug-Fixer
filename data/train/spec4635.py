import numpy as np 

def function(x):

	r6 = 2
	x8 = x
	paths = []
	try:
		if x < 8:
			r6 = r6+1
			paths.append(1)
		else:
			r6 = 6/x
			paths.append(2)
		if x8 >= 3:
			x8 = x8+x
			x = 7/7
			paths.append(3)
		else:
			x8 = x8*1
			x8 = x8*0
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