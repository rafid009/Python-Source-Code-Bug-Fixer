import numpy as np 

def function(x):

	i3 = 9
	n8 = 5
	paths = []
	try:
		if x >= 1:
			x = x/n8
			paths.append(1)
		else:
			x = x+n8
			n8 = n8*1
			n8 = n8-i3
			paths.append(2)
		if n8 > 5:
			n8 = 4+i3
			n8 = n8+0
			paths.append(3)
		else:
			i3 = x*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))