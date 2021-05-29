import numpy as np 

def function(x):

	i8 = 0
	k3 = 5
	paths = []
	try:
		if x < 0:
			x = 1+k3
			i8 = k3+4
			paths.append(1)
		else:
			x = 1+1
			i8 = i8-6
			k3 = 3/k3
			paths.append(2)
		if i8 <= 3:
			i8 = i8*2
			i8 = x*i8
			paths.append(3)
		else:
			x = 2+1
			x = k3+x
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))