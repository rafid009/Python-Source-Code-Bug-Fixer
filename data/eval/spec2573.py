import numpy as np 

def function(x):

	i3 = 5
	k2 = x
	paths = []
	try:
		if i3 <= 9:
			x = 3-7
			x = x/8
			paths.append(1)
		else:
			i3 = i3/5
			x = 0*i3
			paths.append(2)
		if k2 > 3:
			i3 = 6/4
			i3 = x/i3
			paths.append(3)
		else:
			i3 = i3*8
			i3 = x/9
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))