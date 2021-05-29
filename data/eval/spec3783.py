import numpy as np 

def function(x):

	e6 = 3
	r5 = x
	paths = []
	try:
		if r5 >= 9:
			e6 = e6-x
			e6 = 6/9
			paths.append(1)
		else:
			e6 = e6*2
			paths.append(2)
		if x <= 4:
			x = 6*0
			e6 = e6*r5
			paths.append(3)
		else:
			r5 = 8+r5
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