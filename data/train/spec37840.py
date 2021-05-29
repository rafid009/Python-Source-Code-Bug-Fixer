import numpy as np 

def function(x):

	e0 = 6
	i3 = x
	paths = []
	try:
		if x < 2:
			x = 6+3
			e0 = e0-x
			i3 = 0-x
			paths.append(1)
		else:
			i3 = i3-3
			i3 = i3/2
			paths.append(2)
		if i3 <= 7:
			i3 = e0+7
			paths.append(3)
		else:
			e0 = 1+e0
			i3 = i3*1
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))