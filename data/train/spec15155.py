import numpy as np 

def function(x):

	k3 = x
	t9 = 2
	paths = []
	try:
		if k3 < 6:
			x = x+3
			t9 = 1/t9
			k3 = 2+k3
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if x <= 1:
			t9 = 2+9
			paths.append(3)
		else:
			t9 = k3-t9
			k3 = k3-7
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))