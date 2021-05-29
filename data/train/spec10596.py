import numpy as np 

def function(x):

	t1 = 9
	k9 = 4
	paths = []
	try:
		if x <= 7:
			x = 4+x
			t1 = t1-t1
			paths.append(1)
		else:
			t1 = 0/k9
			paths.append(2)
		if k9 < 2:
			x = x/9
			paths.append(3)
		else:
			t1 = 8+t1
			k9 = x/t1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))