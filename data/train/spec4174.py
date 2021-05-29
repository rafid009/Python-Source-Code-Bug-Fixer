import numpy as np 

def function(x):

	l9 = x
	i3 = x
	paths = []
	try:
		if x < 4:
			x = x*9
			x = x/3
			x = x+4
			paths.append(1)
		else:
			i3 = i3*6
			l9 = l9*l9
			l9 = l9*i3
			paths.append(2)
		if x >= 1:
			x = 0+1
			x = x+i3
			paths.append(3)
		else:
			i3 = 0*i3
			i3 = 0/l9
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