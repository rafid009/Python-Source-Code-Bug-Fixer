import numpy as np 

def function(x):

	t9 = x
	k1 = x
	x = 8
	paths = []
	try:
		if t9 < 8:
			x = 8*x
			k1 = 2+t9
			x = x/2
			paths.append(1)
		else:
			t9 = 6+t9
			t9 = t9*k1
			paths.append(2)
		if x > 0:
			x = k1+0
			x = 2/7
			paths.append(3)
		else:
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		t9 = k1**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))