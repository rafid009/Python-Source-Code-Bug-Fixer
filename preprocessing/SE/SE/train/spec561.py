import numpy as np 

def function(x):

	r0 = 7
	q7 = x
	x = 0
	paths = []
	try:
		if x < 7:
			r0 = r0/9
			r0 = r0+r0
			paths.append(1)
		else:
			r0 = r0*r0
			q7 = q7+1
			x = x*2
			paths.append(2)
		if x > 5:
			r0 = r0/7
			r0 = r0-4
			paths.append(3)
		else:
			x = 9-3
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))