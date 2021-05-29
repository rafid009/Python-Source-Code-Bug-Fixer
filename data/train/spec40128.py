import numpy as np 

def function(x):

	k8 = 1
	b8 = x
	paths = []
	try:
		if x >= 9:
			x = x*9
			b8 = b8-x
			k8 = 2+k8
			paths.append(1)
		else:
			k8 = k8*5
			x = x-2
			k8 = 4*k8
			paths.append(2)
		if b8 <= 5:
			k8 = k8/x
			x = 7+x
			paths.append(3)
		else:
			b8 = b8+2
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))