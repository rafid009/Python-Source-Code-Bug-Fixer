import numpy as np 

def function(x):

	t6 = x
	k5 = 9
	paths = []
	try:
		if k5 > 9:
			x = k5+1
			t6 = 3-8
			x = x-6
			paths.append(1)
		else:
			x = x*9
			x = 2+x
			paths.append(2)
		if x <= 4:
			t6 = 8/9
			paths.append(3)
		else:
			k5 = k5*0
			k5 = k5/x
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))