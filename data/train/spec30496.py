import numpy as np 

def function(x):

	x6 = x
	i3 = x
	paths = []
	try:
		if x6 <= 8:
			i3 = i3-4
			paths.append(1)
		else:
			x6 = x6+i3
			x = x+7
			x = x-5
			paths.append(2)
		if x < 7:
			x6 = x6*5
			paths.append(3)
		else:
			x6 = x6-6
			x = 5+1
			i3 = i3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))