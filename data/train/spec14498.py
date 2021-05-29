import numpy as np 

def function(x):

	t5 = 6
	k8 = 6
	paths = []
	try:
		if t5 > 7:
			x = x*k8
			x = 8+x
			k8 = 3/t5
			paths.append(1)
		else:
			k8 = 9/k8
			paths.append(2)
		if k8 < 1:
			k8 = 4+2
			t5 = t5-x
			t5 = 7*t5
			paths.append(3)
		else:
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))