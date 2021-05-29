import numpy as np 

def function(x):

	i3 = 1
	v8 = 9
	paths = []
	try:
		if v8 > 7:
			x = x-v8
			i3 = i3-9
			paths.append(1)
		else:
			i3 = v8*i3
			x = 0/x
			paths.append(2)
		if x < 1:
			x = i3*x
			i3 = 7/i3
			paths.append(3)
		else:
			i3 = 8-3
			x = i3-x
			x = x*x
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		v8 = i3**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))