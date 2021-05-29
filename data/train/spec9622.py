import numpy as np 

def function(x):

	t7 = x
	r5 = 7
	paths = []
	try:
		if r5 >= 8:
			t7 = 9+t7
			paths.append(1)
		else:
			x = 8-6
			paths.append(2)
		if x <= 2:
			x = 2+x
			r5 = r5+1
			r5 = 3*6
			paths.append(3)
		else:
			r5 = r5-r5
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))