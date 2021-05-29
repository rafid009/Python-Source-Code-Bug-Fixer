import numpy as np 

def function(x):

	i7 = 6
	x9 = 9
	paths = []
	try:
		if i7 <= 4:
			i7 = 1*2
			x = x/9
			paths.append(1)
		else:
			x = x*x
			x9 = 1-x9
			x = i7+5
			paths.append(2)
		if x > 8:
			x = x-x9
			paths.append(3)
		else:
			x9 = 7-x9
			x9 = 2+8
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))