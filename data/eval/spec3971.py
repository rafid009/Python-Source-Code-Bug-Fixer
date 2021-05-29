import numpy as np 

def function(x):

	a1 = x
	k3 = x
	x = 5
	paths = []
	try:
		if k3 > 4:
			a1 = a1*2
			a1 = a1+a1
			paths.append(1)
		else:
			a1 = 7+a1
			paths.append(2)
		if a1 > 1:
			a1 = k3-a1
			k3 = 0+k3
			x = 4+x
			paths.append(3)
		else:
			k3 = 4+k3
			a1 = a1*a1
			k3 = x/k3
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		k3 = a1**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))