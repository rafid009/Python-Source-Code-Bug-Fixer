import numpy as np 

def function(x):

	t5 = x
	k3 = x
	x = x
	paths = []
	try:
		if t5 <= 5:
			x = 6-x
			x = x*2
			paths.append(1)
		else:
			x = t5/2
			k3 = 5-k3
			k3 = 3/k3
			paths.append(2)
		if t5 < 2:
			k3 = 1+k3
			x = k3-x
			paths.append(3)
		else:
			x = 1*x
			k3 = 0+x
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t5 = t5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))