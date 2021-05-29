import numpy as np 

def function(x):

	n5 = x
	r3 = x
	paths = []
	try:
		if r3 >= 9:
			r3 = r3/4
			x = r3-x
			x = x*x
			paths.append(1)
		else:
			x = 8*x
			n5 = x-x
			r3 = r3/5
			paths.append(2)
		if x > 4:
			n5 = 7+3
			paths.append(3)
		else:
			n5 = x+x
			x = x*0
			n5 = 4/n5
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))