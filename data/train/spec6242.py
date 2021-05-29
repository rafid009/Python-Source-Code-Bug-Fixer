import numpy as np 

def function(x):

	r1 = x
	l8 = 6
	paths = []
	try:
		if x <= 2:
			r1 = 9/8
			l8 = 8/1
			l8 = r1/l8
			paths.append(1)
		else:
			l8 = 9+0
			x = x/x
			paths.append(2)
		if x > 9:
			r1 = r1*0
			l8 = l8/1
			paths.append(3)
		else:
			r1 = x*2
			x = 9+x
			r1 = x+r1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))