import numpy as np 

def function(x):

	n7 = 6
	r4 = x
	paths = []
	try:
		if r4 <= 5:
			r4 = n7+7
			r4 = x-r4
			x = x*1
			paths.append(1)
		else:
			n7 = n7*1
			paths.append(2)
		if n7 >= 3:
			x = x/x
			n7 = n7-2
			paths.append(3)
		else:
			r4 = r4-n7
			x = r4/8
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		n7 = r4**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))