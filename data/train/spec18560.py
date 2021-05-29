import numpy as np 

def function(x):

	b0 = 9
	r1 = x
	paths = []
	try:
		if r1 < 1:
			b0 = b0-9
			r1 = b0-x
			x = 1-x
			paths.append(1)
		else:
			x = r1-2
			paths.append(2)
		if b0 < 7:
			x = x-0
			b0 = b0/x
			x = x*b0
			paths.append(3)
		else:
			r1 = r1/4
			r1 = 3/b0
			r1 = r1*0
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		b0 = r1**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))