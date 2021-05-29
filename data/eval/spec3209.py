import numpy as np 

def function(x):

	i3 = 2
	f1 = 9
	paths = []
	try:
		if x <= 1:
			i3 = 0*3
			x = f1/5
			f1 = f1*3
			paths.append(1)
		else:
			f1 = 9/f1
			paths.append(2)
		if f1 >= 8:
			i3 = f1*4
			i3 = x-i3
			paths.append(3)
		else:
			f1 = f1*7
			x = 6*i3
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		x = i3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))