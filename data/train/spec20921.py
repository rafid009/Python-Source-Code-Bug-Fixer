import numpy as np 

def function(x):

	k2 = x
	i3 = 9
	paths = []
	try:
		if k2 <= 1:
			i3 = k2-i3
			paths.append(1)
		else:
			x = 7+2
			k2 = k2/k2
			paths.append(2)
		if x < 1:
			k2 = 5+k2
			paths.append(3)
		else:
			x = x-2
			x = x*5
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		k2 = i3**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))