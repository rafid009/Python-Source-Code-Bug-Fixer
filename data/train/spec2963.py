import numpy as np 

def function(x):

	k9 = 5
	t0 = 9
	paths = []
	try:
		if k9 < 3:
			x = 7-k9
			paths.append(1)
		else:
			k9 = x-k9
			t0 = t0-6
			t0 = t0-k9
			paths.append(2)
		if t0 < 5:
			t0 = t0-0
			paths.append(3)
		else:
			x = x*4
			t0 = 9/3
			t0 = x+1
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))