import numpy as np 

def function(x):

	n7 = 9
	r5 = 9
	paths = []
	try:
		if x < 2:
			x = 0+r5
			n7 = n7/n7
			n7 = n7+2
			paths.append(1)
		else:
			r5 = x-7
			n7 = n7+9
			paths.append(2)
		if x < 0:
			n7 = n7-n7
			x = 6+x
			n7 = n7/n7
			paths.append(3)
		else:
			r5 = 2+r5
			n7 = x*1
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))