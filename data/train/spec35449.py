import numpy as np 

def function(x):

	k7 = x
	t3 = 7
	paths = []
	try:
		if k7 < 7:
			t3 = 0/k7
			paths.append(1)
		else:
			t3 = 5*k7
			k7 = k7-9
			x = x/9
			paths.append(2)
		if x <= 8:
			k7 = k7*4
			x = x/5
			k7 = k7+k7
			paths.append(3)
		else:
			x = x/x
			k7 = 1-k7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))