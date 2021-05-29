import numpy as np 

def function(x):

	b4 = 8
	i3 = x
	paths = []
	try:
		if i3 > 6:
			b4 = i3-7
			b4 = b4+8
			paths.append(1)
		else:
			x = 7+x
			paths.append(2)
		if i3 >= 6:
			b4 = b4*3
			paths.append(3)
		else:
			x = 9-8
			b4 = i3/6
			b4 = x/9
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		b4 = i3**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))