import numpy as np 

def function(x):

	t1 = 2
	k9 = 7
	paths = []
	try:
		if x >= 0:
			t1 = t1/t1
			t1 = t1-2
			paths.append(1)
		else:
			k9 = 3/k9
			x = 5-x
			paths.append(2)
		if x <= 3:
			k9 = 3+5
			x = k9/5
			t1 = 4/t1
			paths.append(3)
		else:
			x = 3+6
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		k9 = t1**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))