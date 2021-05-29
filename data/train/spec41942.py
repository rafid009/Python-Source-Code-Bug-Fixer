import numpy as np 

def function(x):

	i3 = x
	k2 = 7
	paths = []
	try:
		if x <= 4:
			i3 = i3-7
			x = x+x
			x = x/k2
			paths.append(1)
		else:
			k2 = x-9
			i3 = 0/6
			paths.append(2)
		if k2 < 4:
			k2 = k2-9
			x = 8-x
			k2 = i3-x
			paths.append(3)
		else:
			k2 = 9-9
			k2 = i3*1
			x = 2+i3
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