import numpy as np 

def function(x):

	t1 = x
	k9 = x
	x = 6
	paths = []
	try:
		if k9 >= 8:
			x = x/5
			k9 = k9+x
			x = x+9
			paths.append(1)
		else:
			k9 = t1*k9
			x = k9-4
			x = 3/t1
			paths.append(2)
		if k9 >= 2:
			t1 = 1-t1
			x = x-k9
			x = t1/1
			paths.append(3)
		else:
			x = t1*5
			t1 = 9/t1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))