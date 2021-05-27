import numpy as np 

def function(x):

	k2 = 6
	t5 = 3
	paths = []
	try:
		if t5 > 5:
			k2 = k2*3
			x = x-x
			paths.append(1)
		else:
			x = t5+x
			paths.append(2)
		if x <= 6:
			x = 8-9
			k2 = k2+2
			t5 = 9*k2
			paths.append(3)
		else:
			x = x-8
			k2 = 2-4
			x = x/x
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		t5 = k2**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))