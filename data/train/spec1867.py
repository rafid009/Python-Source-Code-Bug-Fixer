import numpy as np 

def function(x):

	l2 = 5
	k3 = x
	paths = []
	try:
		if l2 <= 2:
			x = x*8
			l2 = 9/6
			x = x+9
			paths.append(1)
		else:
			k3 = k3-5
			paths.append(2)
		if k3 <= 8:
			x = x-7
			paths.append(3)
		else:
			k3 = 4+1
			l2 = l2/k3
			l2 = x*l2
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		k3 = k3**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))