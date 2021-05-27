import numpy as np 

def function(x):

	f5 = x
	i3 = 9
	paths = []
	try:
		if i3 <= 2:
			x = i3*8
			i3 = i3*x
			f5 = f5/x
			paths.append(1)
		else:
			x = 3/f5
			paths.append(2)
		if x <= 3:
			i3 = i3/1
			paths.append(3)
		else:
			i3 = i3-1
			i3 = i3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))