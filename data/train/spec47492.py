import numpy as np 

def function(x):

	k3 = x
	t3 = 5
	paths = []
	try:
		if t3 <= 2:
			t3 = 0*x
			paths.append(1)
		else:
			x = k3-0
			x = k3/8
			paths.append(2)
		if t3 >= 8:
			x = x-1
			k3 = 0/k3
			paths.append(3)
		else:
			k3 = 9-k3
			t3 = x-t3
			x = x*1
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))