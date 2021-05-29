import numpy as np 

def function(x):

	i2 = x
	i3 = x
	x = x
	paths = []
	try:
		if x < 0:
			i2 = 9*4
			i3 = 6/i3
			paths.append(1)
		else:
			x = 6/5
			x = 8-6
			x = x*4
			paths.append(2)
		if i3 <= 5:
			i2 = 1-0
			x = x-3
			i3 = i3+0
			paths.append(3)
		else:
			i2 = 4-8
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		i3 = i2**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))