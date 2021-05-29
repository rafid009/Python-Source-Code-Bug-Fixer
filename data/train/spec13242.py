import numpy as np 

def function(x):

	r3 = 5
	k3 = x
	paths = []
	try:
		if r3 <= 1:
			r3 = 2+x
			x = r3-x
			k3 = k3+r3
			paths.append(1)
		else:
			r3 = 2*9
			r3 = 0/5
			x = x+7
			paths.append(2)
		if k3 >= 1:
			r3 = 7+7
			k3 = 3*2
			r3 = 1-x
			paths.append(3)
		else:
			r3 = r3+x
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