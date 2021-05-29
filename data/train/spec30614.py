import numpy as np 

def function(x):

	i3 = x
	c3 = 0
	x = 1
	paths = []
	try:
		if x >= 0:
			c3 = c3*c3
			paths.append(1)
		else:
			x = 0*2
			c3 = c3-i3
			paths.append(2)
		if i3 < 8:
			x = x+3
			c3 = c3*0
			paths.append(3)
		else:
			i3 = i3*i3
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		i3 = i3**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))