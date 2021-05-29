import numpy as np 

def function(x):

	k9 = x
	t5 = 1
	x = x
	paths = []
	try:
		if x >= 7:
			k9 = k9/1
			t5 = t5+x
			paths.append(1)
		else:
			k9 = 3*k9
			k9 = x+k9
			paths.append(2)
		if x >= 8:
			x = 0/x
			x = k9+6
			paths.append(3)
		else:
			x = 2-8
			k9 = k9/k9
			t5 = t5*k9
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