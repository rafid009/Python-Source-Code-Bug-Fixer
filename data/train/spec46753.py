import numpy as np 

def function(x):

	u3 = x
	k3 = 5
	paths = []
	try:
		if k3 >= 4:
			k3 = k3+u3
			x = x+1
			u3 = 2/u3
			paths.append(1)
		else:
			k3 = k3-x
			u3 = u3-4
			u3 = u3/4
			paths.append(2)
		if u3 > 4:
			k3 = 2-k3
			k3 = k3+6
			k3 = 5/8
			paths.append(3)
		else:
			k3 = k3-0
			u3 = x-2
			k3 = k3-7
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		k3 = u3**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))