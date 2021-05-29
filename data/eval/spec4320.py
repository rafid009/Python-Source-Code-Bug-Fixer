import numpy as np 

def function(x):

	k3 = x
	b3 = 4
	paths = []
	try:
		if b3 >= 8:
			x = x+6
			x = 3*x
			b3 = b3-4
			paths.append(1)
		else:
			k3 = k3-0
			k3 = k3*8
			x = k3+x
			paths.append(2)
		if k3 < 9:
			x = x-4
			k3 = k3*2
			paths.append(3)
		else:
			b3 = b3*0
			k3 = k3*7
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))