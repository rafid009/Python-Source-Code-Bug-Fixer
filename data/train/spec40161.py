import numpy as np 

def function(x):

	k7 = 1
	t6 = 0
	paths = []
	try:
		if k7 > 1:
			k7 = x+t6
			t6 = 7*5
			paths.append(1)
		else:
			x = 3-x
			k7 = x-k7
			paths.append(2)
		if t6 > 6:
			k7 = k7+t6
			k7 = k7-k7
			t6 = 7*x
			paths.append(3)
		else:
			x = 0/7
			t6 = t6-k7
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))