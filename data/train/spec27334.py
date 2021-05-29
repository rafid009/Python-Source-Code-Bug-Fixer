import numpy as np 

def function(x):

	i5 = 8
	i0 = x
	paths = []
	try:
		if i5 > 3:
			i5 = 2-4
			i5 = 9*i5
			paths.append(1)
		else:
			x = x/5
			x = x/9
			i0 = 7*1
			paths.append(2)
		if i5 < 4:
			i0 = i0+4
			x = x/6
			x = i5/x
			paths.append(3)
		else:
			x = x/i0
			x = x-8
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))