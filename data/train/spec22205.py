import numpy as np 

def function(x):

	k3 = 2
	v9 = 4
	paths = []
	try:
		if v9 < 3:
			k3 = k3*7
			k3 = 1-k3
			x = x+x
			paths.append(1)
		else:
			v9 = x/4
			x = v9-4
			paths.append(2)
		if k3 <= 8:
			k3 = k3-1
			v9 = v9/9
			paths.append(3)
		else:
			k3 = 5*0
			v9 = v9/3
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		k3 = v9**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))