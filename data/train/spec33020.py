import numpy as np 

def function(x):

	i5 = 5
	f0 = 7
	paths = []
	try:
		if f0 <= 5:
			i5 = i5/3
			paths.append(1)
		else:
			i5 = i5+2
			i5 = f0/i5
			paths.append(2)
		if x <= 3:
			f0 = x*f0
			f0 = i5/f0
			paths.append(3)
		else:
			x = f0+x
			x = x-6
			x = x-i5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))