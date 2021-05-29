import numpy as np 

def function(x):

	t3 = x
	k9 = x
	paths = []
	try:
		if x > 3:
			x = x+x
			paths.append(1)
		else:
			k9 = 3/k9
			t3 = 6/5
			t3 = 8-6
			paths.append(2)
		if x >= 4:
			k9 = x/5
			x = x+x
			paths.append(3)
		else:
			t3 = t3-t3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))