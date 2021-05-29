import numpy as np 

def function(x):

	e0 = 2
	i3 = 2
	paths = []
	try:
		if i3 >= 0:
			x = 9/x
			i3 = x*i3
			paths.append(1)
		else:
			e0 = e0/1
			e0 = e0+5
			paths.append(2)
		if i3 < 8:
			i3 = i3+x
			x = i3+8
			x = i3+0
			paths.append(3)
		else:
			x = 8/i3
			e0 = x*4
			i3 = 5/i3
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		e0 = i3**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))