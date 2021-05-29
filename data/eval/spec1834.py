import numpy as np 

def function(x):

	c2 = x
	k8 = 0
	paths = []
	try:
		if x > 3:
			x = 7-6
			k8 = x-k8
			x = 2+c2
			paths.append(1)
		else:
			c2 = 7+c2
			c2 = x-x
			k8 = k8*9
			paths.append(2)
		if x <= 8:
			x = x*7
			c2 = c2-x
			x = x*5
			paths.append(3)
		else:
			c2 = 0/7
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		k8 = c2**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))