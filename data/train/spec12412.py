import numpy as np 

def function(x):

	t7 = 1
	k0 = 5
	paths = []
	try:
		if x < 4:
			x = x*5
			t7 = 6*x
			k0 = 4/k0
			paths.append(1)
		else:
			x = x+8
			t7 = t7/t7
			paths.append(2)
		if t7 < 2:
			x = 7+x
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))