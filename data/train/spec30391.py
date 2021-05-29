import numpy as np 

def function(x):

	r1 = x
	i3 = 3
	paths = []
	try:
		if i3 > 1:
			i3 = i3+i3
			i3 = i3-1
			i3 = r1/i3
			paths.append(1)
		else:
			x = x+8
			x = 9*i3
			i3 = x-1
			paths.append(2)
		if i3 > 3:
			x = x-0
			x = 0+x
			paths.append(3)
		else:
			i3 = i3+5
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		r1 = i3**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))