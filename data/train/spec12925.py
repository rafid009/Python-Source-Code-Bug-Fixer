import numpy as np 

def function(x):

	n4 = 8
	e6 = 2
	paths = []
	try:
		if e6 < 1:
			e6 = 5*1
			x = x*0
			x = x/x
			paths.append(1)
		else:
			e6 = e6-7
			n4 = x+e6
			n4 = x-n4
			paths.append(2)
		if e6 < 7:
			e6 = e6*4
			x = 1*x
			paths.append(3)
		else:
			x = 0+x
			e6 = e6-6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))