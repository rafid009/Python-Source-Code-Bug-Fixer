import numpy as np 

def function(x):

	t6 = 0
	k2 = x
	x = x
	paths = []
	try:
		if t6 >= 0:
			x = 9+x
			x = 8*x
			paths.append(1)
		else:
			x = x+1
			x = 7*x
			k2 = x/k2
			paths.append(2)
		if x <= 5:
			t6 = k2+t6
			paths.append(3)
		else:
			k2 = 8/2
			x = x-t6
			k2 = t6/k2
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		k2 = t6**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))