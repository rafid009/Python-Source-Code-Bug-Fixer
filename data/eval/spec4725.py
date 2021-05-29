import numpy as np 

def function(x):

	k3 = x
	i9 = 2
	x = x
	paths = []
	try:
		if k3 >= 9:
			x = x/7
			x = 5+4
			x = x*2
			paths.append(1)
		else:
			k3 = 1+0
			i9 = x/i9
			k3 = k3-2
			paths.append(2)
		if i9 <= 3:
			x = x*x
			x = i9/i9
			k3 = 1+7
			paths.append(3)
		else:
			x = 8-1
			k3 = 1/6
			x = 2-k3
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))